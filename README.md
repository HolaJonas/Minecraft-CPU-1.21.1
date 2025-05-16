#  Minecraft CPU 1.21+

Do you like **Computer Architecture**… and **Minecraft**?

Then this project might be right up your alley.

This repository includes a Minecraft world (`.zip` file) that contains a fully functional, redstone-based **Minecraft CPU**.

---

## 🔧 Features

- 8 data registers (2 bytes each)
- 16 instruction registers
- Extremely inefficient and slow (*but hey, it works!*)

---

## 📦 Requirements

You'll need the following tools to use and test your own programs:

- [Litematica](https://www.curseforge.com/minecraft/mc-mods/litematica) – For loading schematics
- [WorldEdit](https://enginehub.org/worldedit/) – Optional but helpful

---

## 🚀 Getting Started

1. **Write your program** using the custom instruction set (see below) and save it as a text file.
2. ⚠️ **Note**: The CPU only supports **16 instructions max**. Extra lines will be ignored.
3. Run:

    ```bash
    python MinecraftCPULoader.py
    ```

    Provide:
    - The path to your program file
    - Your Minecraft schematics directory

4. **Launch Minecraft**, enter the provided world, and paste your program schematic into the instruction memory (made of **red wool**).
5. Stop the clock (**lime green wool**), reset the CPU (button next to clock), then restart the clock after a short delay.

---

## 🕓 Speed It Up

- To **speed up execution**, use:

    ```mcfunction
    /tick rate <tickrate>    # Default is 20
    /tick step <in-game-time>
    ```

- If redstone signals seem broken after pasting:

    ```mcfunction
    //reload
    ```

---

## 🧾 Instruction Set

| Instruction        | Format                      | Description                         |
|--------------------|------------------------------|-------------------------------------|
| Load Immediate     | `LI Rdest Imm`               | Load immediate value into register  |
| Add                | `ADD Rdest R1 R2`            | Add two registers                   |
| Subtract           | `SUB Rdest R1 R2`            | Subtract two registers              |
| And                | `AND Rdest R1 R2`            | Bitwise AND                         |
| NAND               | `NAND Rdest R1 R2`           | Bitwise NAND                        |
| Or                 | `OR Rdest R1 R2`             | Bitwise OR                          |
| NOR                | `NOR Rdest R1 R2`            | Bitwise NOR                         |
| XOR                | `XOR Rdest R1 R2`            | Bitwise XOR                         |
| XNOR               | `XNOR Rdest R1 R2`           | Bitwise XNOR                        |
| Shift Right        | `SR Rdest Rsrc`              | Bitwise shift right                 |
| Shift Left         | `SL Rdest Rsrc`              | Bitwise shift left                  |
| Jump to Address    | `JMP Rsrc`                   | Jump to instruction at address      |
| Branch Greater     | `BG Rdest R1 R2`             | Branch if R1 > R2                   |
| Branch Less        | `BL Rdest R1 R2`             | Branch if R1 < R2                   |
| Branch Equal       | `BEQ Rdest R1 R2`            | Branch if R1 == R2                  |
| Branch Not Equal   | `BNE Rdest R1 R2`            | Branch if R1 ≠ R2                   |
| Display Register   | `DSPL Rsrc`                  | Output contents of a register       |

---

## 🧪 Example Program

Multiply 2 and 7, then display the result:

```asm
LI 1 2
LI 2 7
LI 3 1
ADD 4 4 2
SUB 1 1 3
BG 3 1 0
DSPL 4
```
---

## 🪪 License

This project is licensed under the MIT License. Read more [here](LICENSE).
