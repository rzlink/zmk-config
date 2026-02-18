# 🔧 Corne Column Fix Guide

## Problem

Intermittent key failures on **column 5** of the display Corne keyboard.

| Half | Affected Keys | GPIO Pin |
|------|--------------|----------|
| Left | T, G, B, Space | P0.02 |
| Right | Y, H, N, Enter | P0.02 |

**Symptoms:**
- Keys in column 5 stop responding randomly
- Pressing the keyboard case firmly can temporarily restore function
- Issue only affects the display Corne (Mill-Max socketed nice!nano v2)
- Non-display Corne does not have this issue

**Root Cause:** Poor contact between the nice!nano v2 pin and its Mill-Max socket — likely a cold solder joint or oxidized contact on the P0.02 pin position.

---

## Fix Options

### Option 1: Reflow Solder Joints ⭐ Recommended

This is the **permanent fix**. A cold or cracked solder joint on the Mill-Max socket prevents reliable electrical contact.

**Tools needed:**
- Soldering iron (300°C / 570°F)
- Flux (liquid or paste)
- Thin solder wire (0.5mm–0.8mm recommended)
- Solder wick or desoldering pump (optional, for cleanup)

**Steps:**

1. **Power off** — Disconnect USB, remove battery if possible
2. **Remove the nice!nano** — Gently pull it out of the Mill-Max sockets
3. **Flip the PCB** — Locate the Mill-Max socket for the P0.02 pin on the back
   - This is the **5th column pin** — refer to the [Corne pinout diagram](https://docs.typeractive.xyz/build-guides/corne-wireless/troubleshooting)
4. **Apply flux** to the suspect solder joint
5. **Touch with soldering iron** for 2–3 seconds — the existing solder should melt and reflow
6. **Add a tiny bit of fresh solder** if the joint looks thin or dull
7. **Inspect** — A good joint looks smooth, shiny, and concave (volcano shape)
8. **Repeat** for the same pin on the other half
9. **Reinsert** the nice!nano and test

> 💡 **Tip:** While you have the iron out, reflow ALL Mill-Max socket joints — not just the suspect one. This prevents future intermittent failures on other columns.

---

### Option 2: Clean and Reseat

A quick fix that may resolve the issue if caused by oxidation or debris.

**Tools needed:**
- 90%+ isopropyl alcohol
- Cotton swabs or lint-free cloth
- Fine pin or needle

**Steps:**

1. **Remove the nice!nano** from both halves
2. **Clean the nice!nano pins** — Wipe with isopropyl alcohol
3. **Clean inside the Mill-Max sockets** — Use a cotton swab moistened with isopropyl alcohol. Gently insert a fine pin/needle to dislodge any debris
4. **Let dry** completely (1–2 minutes)
5. **Reinsert** the nice!nano firmly and evenly — press straight down, don't rock side to side
6. **Test** all keys in column 5

> ⚠️ This may only be a temporary fix if the root cause is a cold solder joint.

---

### Option 3: Swap Test (Diagnostic)

Use this to confirm whether the issue is the **socket/PCB** or the **nice!nano module**.

**Steps:**

1. Remove the nice!nano from the **display Corne** (broken)
2. Remove the nice!nano from the **non-display Corne** (working)
3. Put the working nice!nano into the display Corne's PCB
4. Test column 5 keys

**Interpreting results:**

| Result | Meaning | Next Step |
|--------|---------|-----------|
| Problem **stays** with the display PCB | Socket/solder issue on PCB | Do Option 1 (reflow) |
| Problem **follows** the nice!nano | Damaged pin on the module | Replace the nice!nano |
| Problem **disappears** | Different pin seating fixed it | Monitor; reflow if it returns |

---

## Reference

### Nice!Nano v2 Pinout

```
        ┌─────────┐
    D1  │ •     • │  RAW
    D0  │ •     • │  GND
   GND  │ •     • │  RST
   GND  │ •     • │  VCC
    D2  │ •     • │  D21
    D3  │ •     • │  D20
    D4  │ •     • │  D19
    D5  │ •     • │  D18
    D6  │ •     • │  D15
    D7  │ •     • │  D14
    D8  │ •     • │  D16
    D9  │ •     • │  D10
        └─────────┘
```

### Corne Column-to-Pin Mapping (nice!nano v2)

| Column | Keys (QWERTY) | GPIO Pin |
|--------|--------------|----------|
| 0 | ` / Tab / Shift (outer) | — |
| 1 | Q, A, Z | P0.22 |
| 2 | W, S, X | P1.11 |
| 3 | E, D, C | P1.13 |
| 4 | R, F, V | P1.15 |
| **5** | **T, G, B** | **P0.02** |
| Thumb 1–3 | Alt, Sym/Esc, Nav/Space | Various |

> The right half is mirrored: column 5 = Y, H, N with the same P0.02 pin.

### Useful Links

- [Typeractive Corne Troubleshooting & Pinouts](https://docs.typeractive.xyz/build-guides/corne-wireless/troubleshooting)
- [Nice!Nano Pinout & Schematic](https://nicekeyboards.com/docs/nice-nano/pinout-schematic/)
- [Nice!Nano Troubleshooting Guide](https://github.com/Nice-Keyboards/nice-keyboards-docs/blob/master/docs/nice!nano/troubleshooting.md)
