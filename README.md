# ZMK Corne Keyboard Configuration

This repository contains my personal ZMK firmware configuration for the Corne (CRKBD) split keyboard using nice!nano v2 controllers.

## Hardware

- **Keyboard**: Corne (CRKBD) 3x6+3 split keyboard
- **Controller**: nice!nano v2 (both halves)
- **Firmware**: ZMK

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
- **DF + GH**: Escape (works on Base, QWERTY, Colemak layers)
- **JK**: Enter (works on most layers)
- **DV**: Backslash
- **KH**: Forward slash
- **JKL**: Toggle between Empty and Games layers

### Custom Behaviors
- **Hold-Tap**: Balanced hold-tap with 200ms tapping term
- **Quick-Tap**: 150ms quick-tap for rapid repeated taps
- **Prior-Idle**: 120ms requirement to prevent accidental holds

## Configuration Files

```
config/
├── corne.conf          # Hardware configuration
├── corne.keymap        # Main keymap definition
├── west.yml           # ZMK project configuration
└── include/
    ├── behaviors.dtsi  # Custom behavior definitions
    ├── combos.dtsi     # Key combination definitions
    └── macros.dtsi     # Custom macro definitions
```

## Build Configuration

The firmware is built for:
- Left half: `nice_nano_v2` + `corne_left`
- Right half: `nice_nano_v2` + `corne_right`

Builds are automated via GitHub Actions as defined in `build.yaml`.

## Customization

### Enabled Features
- Enhanced Bluetooth transmission power (`CONFIG_BT_CTLR_TX_PWR_PLUS_8=y`)
- USB keyboard support (`CONFIG_ZMK_USB=y`)
- USB boot protocol support for BIOS compatibility

### Disabled Features (Commented Out)
- RGB underglow support
- OLED display support

## Installation

1. Fork this repository
2. Customize the keymap in `config/corne.keymap` to your preferences
3. Push changes to trigger GitHub Actions build
4. Download the generated firmware files
5. Flash the appropriate `.uf2` files to each half of your keyboard

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

## Bluetooth Profiles

- Profile 0-4: Available for different devices
- Use maintenance layer to switch profiles
- Clear all profiles option available

## Contributing

Feel free to fork this configuration and adapt it to your needs. If you find improvements or fixes, pull requests are welcome!

## License

This configuration is based on the ZMK firmware project and follows the same MIT license.
