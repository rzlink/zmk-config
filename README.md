# ZMK Corne Keyboard Configuration

This repository contains my personal ZMK firmware configuration for the Corne (CRKBD) split keyboard using nice!nano v2 controllers.

## Generated Keymap

[View all nine layers and their combos](docs/corne.svg).

`docs/corne.svg` is a generated snapshot of the firmware keymap, including
tap/hold legends and layer-specific combos. The **Draw keymap** GitHub Actions
workflow generates fresh YAML/SVG files after relevant pushes and pull requests,
or when run manually. Download its `corne-keymap-diagram` artifact to review them.
The workflow has read-only repository access and never commits updates; refresh
the snapshot manually when changing the keymap.

To regenerate locally with Python 3.13 in PowerShell, from the repository root:

```powershell
$venv = "$env:TEMP\zmk-config-keymap-drawer"
python -m venv $venv
& "$venv\Scripts\python.exe" -m pip install -r docs\keymap-drawer-requirements.txt

& "$venv\Scripts\keymap.exe" -c docs\keymap-drawer.yaml parse -z config\corne.keymap -c 12 -l BASE COLEM SYM FUN NAV GAMES QWERT MAINT EMPTY -o docs\corne.yaml
& "$venv\Scripts\keymap.exe" -c docs\keymap-drawer.yaml draw docs\corne.yaml -k corne_rotated -l LAYOUT_split_3x6_3 -o docs\corne.svg
& "$venv\Scripts\python.exe" docs\validate-keymap.py docs\corne.yaml docs\corne.svg
```

This uses the pinned [Keymap Drawer](https://github.com/caksoylar/keymap-drawer)
version in `docs/keymap-drawer-requirements.txt`. Installation and public layout
downloads require internet access; the keymap is processed locally. Update
`docs/validate-keymap.py` expectations after intentional keymap changes. These
commands only generate documentation, not firmware.

## Hardware

- **Keyboard**: Corne (CRKBD) 3x6+3 split keyboard (42 keys total)
- **Controller**: nice!nano v2 (both halves)
- **Display**: nice!view with the `nice_epaper` shield from `zmk-nice-oled` (optional, one pair)
- **Firmware**: display pair on ZMK v0.3; plain pair on a pinned ZMK development
  snapshot using Zephyr 4.1

## Features

### Layouts
- **Base Layer**: Default QWERTY layout with home row mods
- **Colemak Layer**: Alternative typing layout for improved ergonomics
- **Gaming Layers**: Specialized layouts for gaming with arrow key clusters
- **Symbol Layer**: Easy access to numbers, symbols, and special characters
- **Function Layer**: F-keys (F1-F24), media controls, and system functions
- **Navigation Layer**: Arrow keys, page navigation, virtual desktop switching
- **Maintenance Layer**: Bluetooth profiles, output toggling, and layer management

### Key Features
- **Home Row Mods**: GUI, Alt, Ctrl, and Shift on home row for efficient typing
- **Layer-Tap Keys**: Dual-function keys that act as layer toggles when held
- **Combos**: Key combinations for frequently used actions
- **Custom Macros**: Ubuntu system reboot macro included
- **Bluetooth Support**: 5 profile slots with easy switching
- **USB/Bluetooth Toggle**: Switch between wired and wireless modes

### Layer Details

#### Base Layer (QWERTY) - Layer 0
Standard QWERTY layout with home row modifiers
- Left home row: GUI(A), Alt(S), Ctrl(D), Shift(F)
- Right home row: Shift(J), Ctrl(K), Alt(L), GUI(;)
- Layer access: Symbol(ESC), Navigation(Space/Enter), Function(Tab)

```
╭─────────┬─────────┬─────────┬─────────┬─────────┬─────────╮   ╭─────────┬─────────┬─────────┬─────────┬─────────┬─────────╮
│   `~    │    Q    │    W    │    E    │    R    │    T    │   │    Y    │    U    │    I    │    O    │    P    │   \ |   │
├─────────┼─────────┼─────────┼─────────┼─────────┼─────────┤   ├─────────┼─────────┼─────────┼─────────┼─────────┼─────────┤
│ CTRL/TAB│  GUI/A  │  ALT/S  │ CTRL/D  │ SHFT/F  │    G    │   │    H    │ SHFT/J  │ CTRL/K  │  ALT/L  │ GUI/;:  │   '"    │
├─────────┼─────────┼─────────┼─────────┼─────────┼─────────┤   ├─────────┼─────────┼─────────┼─────────┼─────────┼─────────┤
│  SHIFT  │    Z    │    X    │    C    │    V    │    B    │   │    N    │    M    │   ,<    │   .>    │   /?    │   GUI   │
╰─────────┴─────────┴─────────┼─────────┼─────────┼─────────┤   ├─────────┼─────────┼─────────┼─────────┴─────────┴─────────╯
                              │   ALT   │ SYM/ESC │ NAV/SPC │   │ NAV/ENT │   FUN   │  BKSP   │
                              ╰─────────┴─────────┴─────────╯   ╰─────────┴─────────┴─────────╯
```

#### Colemak Layer - Layer 1
Ergonomic Colemak layout alternative with same modifier positions

```
╭─────────┬─────────┬─────────┬─────────┬─────────┬─────────╮   ╭─────────┬─────────┬─────────┬─────────┬─────────┬─────────╮
│   `~    │    Q    │    W    │    F    │    P    │    B    │   │    J    │    L    │    U    │    Y    │   ;:    │   \ |   │
├─────────┼─────────┼─────────┼─────────┼─────────┼─────────┤   ├─────────┼─────────┼─────────┼─────────┼─────────┼─────────┤
│ CTRL/TAB│  GUI/A  │  ALT/R  │ CTRL/S  │ SHFT/T  │    G    │   │    M    │ SHFT/N  │ CTRL/E  │  ALT/I  │  GUI/O  │   '"    │
├─────────┼─────────┼─────────┼─────────┼─────────┼─────────┤   ├─────────┼─────────┼─────────┼─────────┼─────────┼─────────┤
│  SHIFT  │    Z    │    X    │    C    │    D    │    V    │   │    K    │    H    │   ,<    │   .>    │   /?    │   GUI   │
╰─────────┴─────────┴─────────┼─────────┼─────────┼─────────┤   ├─────────┼─────────┼─────────┼─────────┴─────────┴─────────╯
                              │   ALT   │ SYM/ESC │ NAV/SPC │   │ NAV/ENT │   FUN   │  BKSP   │
                              ╰─────────┴─────────┴─────────╯   ╰─────────┴─────────┴─────────╯
```

#### Symbol Layer - Layer 2
Numbers and symbols with logical positioning

```
╭─────────┬─────────┬─────────┬─────────┬─────────┬─────────╮   ╭─────────┬─────────┬─────────┬─────────┬─────────┬─────────╮
│   `~    │    1    │    2    │    3    │    4    │    5    │   │    6    │    7    │    8    │    9    │    0    │    +    │
├─────────┼─────────┼─────────┼─────────┼─────────┼─────────┤   ├─────────┼─────────┼─────────┼─────────┼─────────┼─────────┤
│  CTRL   │    !    │    @    │    #    │    $    │    %    │   │    ^    │    &    │    *    │    (    │    )    │    =    │
├─────────┼─────────┼─────────┼─────────┼─────────┼─────────┤   ├─────────┼─────────┼─────────┼─────────┼─────────┼─────────┤
│  SHIFT  │    ~    │    -    │    _    │    {    │    }    │   │    [    │    ]    │    <    │    >    │    :    │    ;    │
╰─────────┴─────────┴─────────┼─────────┼─────────┼─────────┤   ├─────────┼─────────┼─────────┼─────────┴─────────┴─────────╯
                              │         │         │  MAINT  │   │  SPACE  │   ALT   │  BKSP   │
                              ╰─────────┴─────────┴─────────╯   ╰─────────┴─────────┴─────────╯
```

#### Function Layer - Layer 3
Complete F1-F24 function key set and system controls

```
╭─────────┬─────────┬─────────┬─────────┬─────────┬─────────╮   ╭─────────┬─────────┬─────────┬─────────┬─────────┬─────────╮
│  CAPS   │   F12   │   F7    │   F8    │   F9    │  PRINT  │   │   F13   │   F14   │   F15   │   F16   │   F17   │   F18   │
├─────────┼─────────┼─────────┼─────────┼─────────┼─────────┤   ├─────────┼─────────┼─────────┼─────────┼─────────┼─────────┤
│  CTRL   │   F11   │   F4    │   F5    │   F6    │  SCRLK  │   │   F19   │   F20   │   F21   │   F22   │   F23   │   F24   │
├─────────┼─────────┼─────────┼─────────┼─────────┼─────────┤   ├─────────┼─────────┼─────────┼─────────┼─────────┼─────────┤
│  SHIFT  │   F10   │   F1    │   F2    │   F3    │  BREAK  │   │   INS   │   DEL   │         │         │         │         │
╰─────────┴─────────┴─────────┼─────────┼─────────┼─────────┤   ├─────────┼─────────┼─────────┼─────────┴─────────┴─────────╯
                              │  CTRL   │   ALT   │   DEL   │   │         │         │         │
                              ╰─────────┴─────────┴─────────╯   ╰─────────┴─────────┴─────────╯
```

#### Navigation Layer - Layer 4
Arrow keys, page navigation, and virtual desktop switching

```
╭─────────┬─────────┬─────────┬─────────┬─────────┬─────────╮   ╭─────────┬─────────┬─────────┬─────────┬─────────┬─────────╮
│   GUI   │         │         │   END   │         │ SCRN_L  │   │  HOME   │  PG_DN  │  PG_UP  │   END   │   UP    │         │
├─────────┼─────────┼─────────┼─────────┼─────────┼─────────┤   ├─────────┼─────────┼─────────┼─────────┼─────────┼─────────┤
│  CTRL   │  HOME   │         │         │  RIGHT  │ SCRN_R  │   │  LEFT   │  DOWN   │   UP    │  RIGHT  │         │         │
├─────────┼─────────┼─────────┼─────────┼─────────┼─────────┤   ├─────────┼─────────┼─────────┼─────────┼─────────┼─────────┤
│  SHIFT  │         │         │         │         │  LEFT   │   │  DOWN   │         │         │         │         │         │
╰─────────┴─────────┴─────────┼─────────┼─────────┼─────────┤   ├─────────┼─────────┼─────────┼─────────┴─────────┴─────────╯
                              │  CTRL   │   ALT   │  SHIFT  │   │  SHIFT  │   ALT   │  CTRL   │
                              ╰─────────┴─────────┴─────────╯   ╰─────────┴─────────┴─────────╯
```

#### Games Layer - Layer 5
Dedicated arrow key clusters for gaming

```
╭─────────┬─────────┬─────────┬─────────┬─────────┬─────────╮   ╭─────────┬─────────┬─────────┬─────────┬─────────┬─────────╮
│         │         │         │   UP    │         │         │   │         │         │   UP    │         │         │         │
├─────────┼─────────┼─────────┼─────────┼─────────┼─────────┤   ├─────────┼─────────┼─────────┼─────────┼─────────┼─────────┤
│  CTRL   │         │  LEFT   │  DOWN   │  RIGHT  │         │   │         │  LEFT   │  DOWN   │  RIGHT  │         │  CTRL   │
├─────────┼─────────┼─────────┼─────────┼─────────┼─────────┤   ├─────────┼─────────┼─────────┼─────────┼─────────┼─────────┤
│  QWERT  │         │         │         │         │         │   │         │         │         │         │         │  QWERT  │
╰─────────┴─────────┴─────────┼─────────┼─────────┼─────────┤   ├─────────┼─────────┼─────────┼─────────┴─────────┴─────────╯
                              │   ESC   │  SPACE  │  ENTER  │   │  ENTER  │  SPACE  │   ESC   │
                              ╰─────────┴─────────┴─────────╯   ╰─────────┴─────────┴─────────╯
```

#### QWERTY Layer - Layer 6
Pure QWERTY for gaming (no home row mods)

```
╭─────────┬─────────┬─────────┬─────────┬─────────┬─────────╮   ╭─────────┬─────────┬─────────┬─────────┬─────────┬─────────╮
│   `~    │    Q    │    W    │    E    │    R    │    T    │   │    Y    │    U    │    I    │    O    │    P    │   \ |   │
├─────────┼─────────┼─────────┼─────────┼─────────┼─────────┤   ├─────────┼─────────┼─────────┼─────────┼─────────┼─────────┤
│ CTRL/TAB│    A    │    S    │    D    │    F    │    G    │   │    H    │    J    │    K    │    L    │   ;:    │   '"    │
├─────────┼─────────┼─────────┼─────────┼─────────┼─────────┤   ├─────────┼─────────┼─────────┼─────────┼─────────┼─────────┤
│  SHIFT  │    Z    │    X    │    C    │    V    │    B    │   │    N    │    M    │   ,<    │   .>    │   /?    │         │
╰─────────┴─────────┴─────────┼─────────┼─────────┼─────────┤   ├─────────┼─────────┼─────────┼─────────┴─────────┴─────────╯
                              │   ALT   │   ESC   │  SPACE  │   │  ENTER  │   DEL   │  BKSP   │
                              ╰─────────┴─────────┴─────────╯   ╰─────────┴─────────┴─────────╯
```

#### Maintenance Layer - Layer 7
System controls, Bluetooth profiles, and layer toggles

```
╭─────────┬─────────┬─────────┬─────────┬─────────┬─────────╮   ╭─────────┬─────────┬─────────┬─────────┬─────────┬─────────╮
│ BT_CLR  │         │         │         │  BT_3   │  BT_0   │   │  VOL+   │         │         │         │         │ BRGHT+  │
├─────────┼─────────┼─────────┼─────────┼─────────┼─────────┤   ├─────────┼─────────┼─────────┼─────────┼─────────┼─────────┤
│ T_EMPTY │ T_GAMES │         │         │  BT_4   │  BT_1   │   │  VOL-   │         │         │         │         │ BRGHT-  │
├─────────┼─────────┼─────────┼─────────┼─────────┼─────────┤   ├─────────┼─────────┼─────────┼─────────┼─────────┼─────────┤
│ T_COLEM │         │         │         │         │  BT_2   │   │  MUTE   │         │         │         │         │ OUT_TOG │
╰─────────┴─────────┴─────────┼─────────┼─────────┼─────────┤   ├─────────┼─────────┼─────────┼─────────┴─────────┴─────────╯
                              │         │         │         │   │         │         │         │
                              ╰─────────┴─────────┴─────────╯   ╰─────────┴─────────┴─────────╯
```

#### Empty Layer - Layer 8
Disabled layer (all keys inactive)

```
╭─────────┬─────────┬─────────┬─────────┬─────────┬─────────╮   ╭─────────┬─────────┬─────────┬─────────┬─────────┬─────────╮
│         │         │         │         │         │         │   │         │         │         │         │         │         │
├─────────┼─────────┼─────────┼─────────┼─────────┼─────────┤   ├─────────┼─────────┼─────────┼─────────┼─────────┼─────────┤
│         │         │         │         │         │         │   │         │         │         │         │         │         │
├─────────┼─────────┼─────────┼─────────┼─────────┼─────────┤   ├─────────┼─────────┼─────────┼─────────┼─────────┼─────────┤
│         │         │         │         │         │         │   │         │         │         │         │         │         │
╰─────────┴─────────┴─────────┼─────────┼─────────┼─────────┤   ├─────────┼─────────┼─────────┼─────────┴─────────┴─────────╯
                              │         │         │         │   │         │         │         │
                              ╰─────────┴─────────┴─────────╯   ╰─────────┴─────────┴─────────╯
```

### Combos
Combos use physical key positions, not the characters emitted by the active layer.
All combos have a 30 ms timeout. The position grid is in `config/include/combos.dtsi`.

| Positions | QWERTY positions | Colemak positions | Action | Active layers |
|-----------|-----------------|-------------------|--------|---------------|
| 15 + 16 | D + F | S + T | Escape | BASE, QWERT, COLEM |
| 19 + 20 | J + K | N + E | Enter | BASE, QWERT, COLEM, SYM, GAMES |
| 15 + 28 | D + V | S + D | Backslash | BASE, QWERT, COLEM |
| 20 + 31 | K + M | E + H | Forward slash | BASE, QWERT, COLEM |
| 19 + 20 + 21 | J + K + L | N + E + I | Toggle EMPTY off | EMPTY |
| 19 + 20 + 21 | J + K + L | N + E + I | Toggle GAMES off | GAMES |

The three-key combos exit their respective layer, revealing whichever layers remain
active underneath; they do not switch directly between GAMES and EMPTY.

### Custom Behaviors
- **Hold-Tap (ht)**: Unified balanced hold-tap behavior for all home row modifiers
  - **Flavor**: Balanced (requires second key release while modifier held)
  - **Tapping Term**: 280ms
  - **Quick-Tap**: 175ms for rapid repeated taps
  - **Prior-Idle**: 150ms requirement to prevent accidental holds during fast typing
  - **Hold-Trigger-on-Release**: Evaluates positional hold-tap restrictions on the other key's release rather than press
  - **Hold-Trigger-Key-Positions**: All 42 positions allowed; no opposite-hand restriction is imposed

#### Home Row Mod Configuration
The configuration uses a single unified hold-tap behavior optimized for reliability:
- All modifiers (Shift, Ctrl, Alt, GUI) use the same `ht` behavior with 280ms tapping term
- `require-prior-idle-ms=150` favors taps after recent typing to reduce accidental modifiers
- Works with both same-hand and cross-hand key combinations (e.g., F+N for "N", J+I for "I")

Thumb layer-taps (`SYM_ESC`, `NAV_SPC`, `NAV_ENT`) and mod-taps such as
`LCTRL_TAB` use the separate upstream `&lt`/`&mt` defaults, not these `&ht`
settings. Their behavior and the existing combo timings are unchanged.

## Configuration Files

```
config/
├── corne.conf          # Hardware configuration
├── corne_left.conf     # Central-only USB and peripheral battery reporting
├── corne_right.conf    # Override the board's USB keyboard default on the peripheral
├── corne.keymap        # Main keymap definition
├── west.yml           # ZMK project configuration
└── include/
    ├── behaviors.dtsi  # Custom behavior definitions
    ├── combos.dtsi     # Key combination definitions
    └── macros.dtsi     # Custom macro definitions
```

`config-plain/west.yml` selects the newer ZMK revision without the display
module. Its `corne.keymap` includes `config/corne.keymap`; edit the shared
keymap, not a second copy. `build-plain.yaml` loads the shared `corne.conf`
and the appropriate half-specific `.conf` via `EXTRA_CONF_FILE`.

## Build Configuration

Two independent workflow runs build the keyboard pairs. Their artifacts are
isolated because the upstream reusable workflow merges all `artifact-*`
uploads in its run.

| Pair | Workflow | Matrix | Download |
|------|----------|--------|----------|
| Plain | Build plain firmware (Zephyr 4.1) | `build-plain.yaml` | `firmware-plain-zephyr41` |
| Display | Build display firmware (ZMK v0.3) | `build.yaml` | `firmware-display-zmk03` |

### Plain Builds (no display, Zephyr 4.1)
- Left half: `nice_nano//zmk` + `corne_left` -> `plain-zephyr41-corne_left.uf2`
- Right half: `nice_nano//zmk` + `corne_right` -> `plain-zephyr41-corne_right.uf2`

The plain track pins ZMK and its reusable workflow to development commit
`641514a97db345f499dd50b0360e594270f008fe`, whose manifest uses Zephyr
`v4.1.0+zmk-fixes`. This is not a stable ZMK release. Keep the revision in
`config-plain/west.yml` and `.github/workflows/build-plain.yml` in sync.

### Display Builds (with nice!view, ZMK v0.3)
- Left half: `nice_nano_v2` + `corne_left` + `nice_view_adapter` + `nice_epaper`
- Right half: `nice_nano_v2` + `corne_right` + `nice_view_adapter` + `nice_epaper`

Files are named `display-zmk03-corne_left.uf2` and
`display-zmk03-corne_right.uf2`. The ZMK revision in `config/west.yml` and workflow tag in
`.github/workflows/build.yml` must be upgraded together. The display module is
pinned to commit `46f824abb2bd41f1287c5c68abd14122af6042a3` to prevent upstream
changes from unexpectedly changing the display build.

### Settings Reset

Each track includes its own `settings_reset` build, named
`plain-zephyr41-settings_reset.uf2` or `display-zmk03-settings_reset.uf2`.
These clear settings; they are not normal keyboard firmware and do not load
the shared Corne keymap or `.conf` files.

**Flash both halves of a physical keyboard from the same track.** Do not mix a
Zephyr 4.1 left half with a ZMK v0.3 right half. Keep the previous working UF2
files when trying the development track so both halves can be rolled back.

## Customization

### Enabled Features
- Enhanced Bluetooth transmission power (`CONFIG_BT_CTLR_TX_PWR_PLUS_8=y`)
- USB keyboard and BIOS boot protocol support on the left/central half,
  configured in `corne_left.conf`. The right half sends keys over Bluetooth
  to the left; connecting its USB cable still supports charging and flashing.
  `corne_right.conf` explicitly disables `CONFIG_ZMK_USB` to override the
  nice!nano board's enabled default and avoid a Kconfig dependency warning.
- Deep sleep after 15 minutes of inactivity (`CONFIG_ZMK_SLEEP=y`,
  `CONFIG_ZMK_IDLE_SLEEP_TIMEOUT=900000`). Press a key to wake; allow time for
  Bluetooth to reconnect. The existing idle timeout is unchanged.
- Right-half battery fetching and Bluetooth proxy reporting on the left/central
  half. Both tracks load `corne_left.conf` in addition to the shared `corne.conf`,
  so these central-only options do not apply to right-half or settings-reset builds.

### Display Configuration
- nice!view display support uses the `nice_epaper` shield from
  [mctechnology17/zmk-nice-oled](https://github.com/mctechnology17/zmk-nice-oled).
  Its upstream README documents testing with ZMK v0.3.0.
- The shield enables the display and custom status screen only for display
  builds; plain builds remain display-free. No global display flags are needed
  in `corne.conf`.
- The left display shows the active layer, battery and connection/profile
  information. All nine layers have short `display-name` labels. The right
  display uses the module's default cat animation and local status widgets.
- Each display shows its own battery with the default settings. The module
  supports optional combined battery widgets, but those are not enabled by
  this configuration.
- Unlike the previous Luffy screen, `nice_epaper` defaults to blanking on idle.
  The existing idle timeout and 15-minute deep-sleep setting are unchanged.
- Battery proxy reporting exposes the right battery through an additional BLE
  Battery Service. Many host battery menus show only one battery; displaying
  both may require a compatible application.

### Disabled Features (Commented Out)
- RGB underglow support
- Built-in OLED display support (using nice!view instead)

## Installation

1. Fork this repository
2. Customize the keymap in `config/corne.keymap` to your preferences
3. Push changes to trigger both GitHub Actions firmware workflows
4. Download the artifact for your plain or display keyboard from the table above
5. Flash the left and right `.uf2` files from the same track (not `settings_reset`)

## Troubleshooting

### Hardware Issues
If you're experiencing intermittent key failures, especially with Mill-Max socketed nice!nano controllers, see the [Column Fix Guide](docs/column-fix-guide.md) for detailed troubleshooting steps.

### Home Row Mods
The current configuration uses a unified hold-tap behavior that works well for most typing styles. If you experience issues:
- Adjust `require-prior-idle-ms` in `config/include/behaviors.dtsi` (currently 150ms)
- Increase `tapping-term-ms` if you find holds aren't triggering (currently 280ms)
- Adjust `quick-tap-ms` for faster repeated taps (currently 175ms)

## Layer Reference

| Layer | Number | Purpose |
|-------|--------|---------|
| BASE  | 0 | Default QWERTY with home row mods |
| COLEMAK | 1 | Alternative typing layout |
| SYMBOL | 2 | Numbers and symbols |
| FUNCTION | 3 | F-keys and system functions |
| NAVIGATION | 4 | Arrow keys and page navigation |
| GAMES | 5 | Gaming-optimized layout |
| QWERTY | 6 | Pure QWERTY for gaming |
| MAINTENANCE | 7 | System controls and toggles |
| EMPTY | 8 | Disabled layer |

The displayed `EMPTY` layer uses the firmware constant `LAYER_EMPTY` to avoid
colliding with Zephyr's `EMPTY` macro. Its index and bindings are unchanged.

## Bluetooth Profiles

- Profile 0-4: Available for different devices
- Use maintenance layer to switch profiles
- `BT_CLR` clears only the selected profile. Select each profile in turn to
  clear multiple pairings; the settings-reset firmware clears on-device settings.

## Contributing

Feel free to fork this configuration and adapt it to your needs. If you find improvements or fixes, pull requests are welcome!

## License

This configuration is based on the ZMK firmware project and follows the same MIT license.
