# Project 5: Simple Python Calculator

A robust, interactive, command-line Python calculator that supports basic arithmetic, advanced operations, calculation chaining, and session history

## Features

- **Core Arithmetic**: Supports addition (`+`), subtraction (`-`), multiplication (`*`), and division (`/` or `÷`).
- **Stretch Operations**: Supports exponentiation (`^`) and modulus (`%`).
- **Flexible Number Formats**: Accepts integers and decimals (e.g., `3`, `3.5`, or `3,5` with commas).
- **Session History**: Stores all past equations in an interactive memory list .
- **Chained Calculations**: Allows using the previous calculation's result as the first number of the next calculation by simply pressing `Enter`.
- **Crash-Resilient Parser**: Validates all inputs to elegantly handle bad data, division by zero, overflow errors, and improper operators without crashing.
- **Coloured Terminal Output**: Enhanced with ANSI color escapes to visually separate results (green), errors (red), and system updates (cyan).

---

## File Structure

- `calculator.py`: The single executable file containing the interactive input loop, calculation logic, validation, and session history management.

---

## Installation & How to Run

No external dependencies or packages are required. The project runs on standard Python 3.

To run the calculator, open your terminal and execute:

```bash
python calculator.py
```
OR
```bash
python3 calculator.py
```

---

## Supported Commands

The interactive input loop accepts numeric values, operators, and special control commands:

- **`exit`** or **`quit`**: Terminate the calculator session.
- **`history`**: Display a formatted list of all past equations performed in the current session.
- **`clear`**: Reset the calculator memory, clear the calculation history, and start fresh.

---

## Step-by-Step Usage Example

Here is a typical execution flow demonstrating chaining and command capabilities:

```text
========================================
   COMMAND-LINE CALCULATOR (v1.0.0)
========================================
Type 'exit' or 'quit' to close.
Type 'history' to view past calculations.
Type 'clear' to reset calculator memory.
========================================

Enter first number (or press Enter to use previous): 5
Enter operator (+, -, *, /, ^, %): *
Enter second number: 1.5

Result: 5.0 * 1.5 = 7.50

Enter first number (or press Enter to use previous): [Press Enter]
Using previous result: 7.5
Enter operator (+, -, *, /, ^, %): ^
Enter second number: 2

Result: 7.5 ^ 2.0 = 56.25

Enter first number (or press Enter to use previous): history

--- Calculation History ---
1. 5.0 * 1.5 = 7.5
2. 7.5 ^ 2.0 = 56.25
---------------------------

Enter first number (or press Enter to use previous): exit
Goodbye!
```

---

## Robust Error Handling & Edge Cases Checked

The calculator parser and execution blocks safeguard the runtime against common edge cases:

1. **Division or Modulo by Zero**: Traps division/modulo by zero and returns a friendly notice rather than crashing the program.
2. **Whitespace Stripping**: Auto-trims input strings (e.g., `"  5.2  "` is parsed safely as `5.2`).
3. **Invalid Operations**: Rejects unsupported inputs elegantly and prompts the user to try again.
4. **Alphabetic Entries**: Gracefully flags inputs like `"abc"` without raising unhandled runtime `ValueError` exceptions.
5. **Float Overflow**: Prevents extremely large exponential computations from crashing the interface due to Python float limits.

---

