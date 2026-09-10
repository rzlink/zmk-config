# Copilot instructions for this ZMK config

This repo is a [ZMK](https://zmk.dev) firmware configuration for a **Corne (CRKBD)**
split keyboard. It contains keymaps and device-tree config, not application code.

## Build, test, verify

- **There is no local build, test, or lint step.** Firmware is compiled by GitHub
  Actions only.
- `.github/workflows/build.yml` reuses `zmkfirmware/zmk/.github/workflows/build-user-config.yml@v0.3`.
- The build matrix lives in `build.yaml` (repo root) as `include:` entries of
  `board` + `shield` combinations.
- To verify a change: push (or open a PR), let the workflow run, and download the
  `.uf2` artifacts. Flash one `.uf2` to each keyboard half.
- **ZMK is pinned to `v0.3`.** The revision in `config/west.yml` and the workflow tag
  must stay in sync; bump both together when upgrading.

## Architecture

- `config/corne.keymap` — the main keymap. Defines 9 layers, each as a
  `<name>_layer { bindings = <...>; }` node inside the single `/ { keymap { ... } }`
  device-tree node. Layer indices are `#define` constants at the top of the file
  (`BASE COLEM SYM FUN NAV GAMES QWERT MAINT LAYER_EMPTY`).
- `config/include/` — fragments `#include`d *inside* the `/ { ... }` node of the keymap
  (see the top of `corne.keymap`):
  - `behaviors.dtsi` — custom behaviors: `&ht` (home-row hold-tap) and `mo_sl`.
    Tuning lives here (`TAPPING_TERM`, `QUICK_TAP_TERM`, trigger positions).
  - `combos.dtsi` — combos via the `COMBO(name, timeout, keys, bindings, layers)` macro.
    The 0–41 key-position grid is documented in a comment at the top of this file.
  - `macros.dtsi` — ZMK behavior macros (e.g. `ubuntu_reboot`).
- `config/corne.conf` — shared Bluetooth and sleep configuration; RGB and OLED
  display options are commented out.
- `config/corne_left.conf` — central-only USB and peripheral battery reporting.
- `config/corne_right.conf` — disables the board's USB keyboard default on the peripheral.
- `config/west.yml` — west manifest; imports `zmk` plus the pinned `zmk-nice-oled`
  display module from the `mctechnology17` remote.
- `docs/column-fix-guide.md` — hardware troubleshooting only, unrelated to firmware code.

## Conventions

- **Reference layers and complex bindings by `#define` alias, never raw numbers or
  inline behaviors.** Home-row mods, layer-taps, and mod-taps are all aliased at the top
  of `corne.keymap` (e.g. `LGUI_A`, `SYM_ESC`, `LCTRL_TAB`). Add a new `#define` rather
  than inlining `&ht`/`&lt`/`&mt` in a layer.
- **Keep the ASCII box-drawing alignment** in each layer. Bindings are laid out as a
  6×3 + 3-thumb grid with matching comment templates above each row; preserve the column
  spacing when editing.
- Combos use the 0–41 key-position numbering from the diagram in `combos.dtsi`, and list
  the layers (by `#define` name) on which they are active.
- When adding a layer, update the layer `#define` block, add the `_layer` node, and check
  whether combos/behaviors need the new layer name — a new `build.yaml` entry is only
  needed for a new board/shield combo (rarely).
- **Display builds** require both the `nice_view_adapter` and `nice_epaper` shields
  in the `build.yaml` entry; plain builds omit them. There is also a `settings_reset`
  build for clearing on-device settings.

See `README.md` for the full per-layer reference and hardware details.
