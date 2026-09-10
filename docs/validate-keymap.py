"""Regression checks for drawer output; update expectations after intentional keymap changes."""

import argparse
from collections import Counter
from pathlib import Path
import xml.etree.ElementTree as ET

import yaml


LAYERS = "BASE COLEM SYM FUN NAV GAMES QWERT MAINT EMPTY".split()
COMBOS = [
    ([15, 16], "ESCAPE", "", ["BASE", "QWERT", "COLEM"]),
    ([19, 20], "RETURN", "", ["BASE", "QWERT", "COLEM", "SYM", "GAMES"]),
    ([15, 28], "\\", "", ["BASE", "QWERT", "COLEM"]),
    ([20, 31], "/", "", ["BASE", "QWERT", "COLEM"]),
    ([19, 20, 21], "EMPTY", "toggle", ["EMPTY"]),
    ([19, 20, 21], "GAMES", "toggle", ["GAMES"]),
]


def legends(key):
    return (key.get("t", ""), key.get("h", "")) if isinstance(key, dict) else (str(key), "")


def validate(data, svg):
    def require(condition, message):
        if not condition:
            raise ValueError(message)

    require(list(data["layers"]) == LAYERS, "Expected all nine layers in firmware order")
    layers = {}
    for name, rows in data["layers"].items():
        keys = [key for row in rows for key in (row if isinstance(row, list) else [row])]
        require(len(keys) == 42, f"{name}: expected 42 bindings, got {len(keys)}")
        layers[name] = keys

    # These aliases exercise &mt, custom &ht from the include, and &lt layer numbers.
    for name, taps in (("BASE", "ASDFJKL;"), ("COLEM", "ARSTNEIO")):
        positions = [13, 14, 15, 16, 19, 20, 21, 22]
        holds = "LGUI LALT LCTRL LSHIFT RSHIFT RCTRL RALT RGUI".split()
        for pos, tap, hold in zip(positions, taps, holds):
            require(legends(layers[name][pos]) == (tap, hold), f"{name}[{pos}]: lost home-row tap/hold")
        for pos, expected in {12: ("TAB", "LCTRL"), 37: ("ESC", "SYM"),
                              38: ("SPACE", "NAV"), 39: ("RET", "NAV")}.items():
            require(legends(layers[name][pos]) == expected, f"{name}[{pos}]: lost aliased tap/hold")
    require(legends(layers["QWERT"][12]) == ("TAB", "LCTRL"), "QWERT: lost Ctrl/Tab")

    combos = data.get("combos", [])
    actual = [(combo["p"], *legends(combo["k"]), combo.get("l", [])) for combo in combos]
    require(actual == COMBOS, "Combo positions, actions, or active layers differ from firmware expectations")

    ns = {"svg": "http://www.w3.org/2000/svg"}
    groups = svg.findall(".//svg:g", ns)
    layer_groups = [group for group in groups if group.get("class", "").startswith("layer-")]
    require(len(layer_groups) == 9, "SVG must contain nine layer diagrams")
    expected_combos = Counter(layer for combo in combos for layer in combo["l"])
    for name, group in zip(LAYERS, layer_groups):
        require(group.get("class") == f"layer-{name}", f"SVG: missing or out-of-order {name}")
        children = group.findall(".//svg:g", ns)
        keys = [node for node in children if "key" in node.get("class", "").split()]
        drawn_combos = [node for node in children if "combo" in node.get("class", "").split()]
        require(len(keys) == 42, f"SVG {name}: expected 42 keys")
        require(len(drawn_combos) == expected_combos[name], f"SVG {name}: incorrect combo count")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("yaml", type=Path)
    parser.add_argument("svg", type=Path)
    args = parser.parse_args()
    validate(yaml.safe_load(args.yaml.read_text(encoding="utf-8")), ET.parse(args.svg).getroot())
    print("Validated nine 42-key layers, aliased tap/holds, and all six layer-scoped combos in YAML/SVG.")
