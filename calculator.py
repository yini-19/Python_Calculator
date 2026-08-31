#!/usr/bin/env python3
"""
Simple Python Calculator
A robust, modular, and terminal-friendly command-line calculator.
Developed as Project 5 ("NotebookLM Vibe Coding") with Gemini Notebook.
"""

import sys

# ANSI Escape Sequences for terminal styling (supported in most terminals)
COLOR_RESET = "\033[0m"
COLOR_BOLD = "\033[1m"
COLOR_GREEN = "\033[32m"
COLOR_RED = "\033[31m"
COLOR_CYAN = "\033[36m"
COLOR_YELLOW = "\033[33m"

def print_success(message: str):
    """Print formatted success message in green."""
    print(f"{COLOR_GREEN}{message}{COLOR_RESET}")

def print_error(message: str):
    """Print formatted error message in bold red."""
    print(f"{COLOR_RED}{COLOR_BOLD}Error: {message}{COLOR_RESET}")

def print_info(message: str):
    """Print formatted info message in cyan."""
    print(f"{COLOR_CYAN}{message}{COLOR_RESET}")

def print_header(message: str):
    """Print styled header in bold yellow."""
    print(f"\n{COLOR_YELLOW}{COLOR_BOLD}=== {message} ==={COLOR_RESET}")


# ==========================================
# 1. MATHEMATICAL OPERATIONS
# ==========================================

def add(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b

def subtract(a: float, b: float) -> float:
    """Return the difference between two numbers."""
    return a - b

def multiply(a: float, b: float) -> float:
    """Return the product of two numbers."""
    return a * b

def divide(a: float, b: float) -> float:
    """
    Return the quotient of two numbers.
    Raises ZeroDivisionError if b is zero.
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b

def power(a: float, b: float) -> float:
    """Return 'a' raised to the power of 'b'."""
    return a ** b

def modulus(a: float, b: float) -> float:
    """
    Return the remainder of dividing 'a' by 'b'.
    Raises ZeroDivisionError if b is zero.
    """
    if b == 0:
        raise ZeroDivisionError("Modulo by zero is undefined.")
    return a % b


# ==========================================
# 2. INPUT VALIDATION & PARSING
# ==========================================

def clean_input(prompt: str) -> str:
    """Prompt the user for input and return a stripped, lowercase version."""
    try:
        user_in = input(prompt)
        return user_in.strip()
    except (KeyboardInterrupt, EOFError):
        # Gracefully capture keyboard interrupts and treat them as an exit command
        print("\n")
        return "exit"

def parse_number(value_str: str) -> float:
    """
    Parse a string into a float.
    Raises ValueError if conversion fails.
    """
    # Replace comma with dot if the user types e.g. "3,5"
    normalized_str = value_str.replace(",", ".")
    return float(normalized_str)

def parse_operator(op_str: str) -> str:
    """
    Validate and normalize the arithmetic operator.
    Supports: +, -, *, /, ÷, %, ^
    Raises ValueError if unsupported.
    """
    valid_operators = {
        "+": "+",
        "-": "-",
        "*": "*",
        "/": "/",
        "÷": "/",
        "%": "%",
        "^": "^"
    }
    
    if op_str in valid_operators:
        return valid_operators[op_str]
    raise ValueError(f"Invalid operator '{op_str}'. Supported operators: +, -, *, /, ÷, %, ^")


# ==========================================
# 3. HISTORY TRACKER
# ==========================================

class CalculationHistory:
    """Manages past calculations in an in-memory list."""
    def __init__(self):
        self.history = []

    def add_entry(self, num1: float, op: str, num2: float, result: float):
        """Format and append a successful calculation to the history log."""
        # Convert floats to integers if they have no decimal fractional part for cleaner printing
        n1 = int(num1) if num1.is_integer() else num1
        n2 = int(num2) if num2.is_integer() else num2
        res = int(result) if result.is_integer() else result
        
        entry = f"{n1} {op} {n2} = {res}"
        self.history.append(entry)

    def display(self):
        """Display the complete session history list."""
        if not self.history:
            print_info("No calculations have been made yet in this session.")
            return
        
        print_header("Calculation History")
        for idx, entry in enumerate(self.history, start=1):
            print(f"  [{idx}] {entry}")
        print()

    def clear(self):
        """Clear the history log."""
        self.history.clear()
        print_info("Calculation history cleared.")


# ==========================================
# 4. MAIN CONTROLLER LOOP
# ==========================================

def run_calculator():
    """Main CLI loop that manages inputs, calculation dispatching, and state."""
    history_manager = CalculationHistory()
    last_result = None  # Holds the result of the previous operation for chaining
    
    print_header("Interactive CLI Python Calculator")
    print("Welcome to Project 5: NotebookLM Vibe Coding!")
    print("Supported Operators: Addition (+), Subtraction (-), Multiplication (*), Division (/, ÷)")
    print("Stretch Operators: Exponent (^), Modulus (%)")
    print("Special Commands:")
    print("  'history' - View past calculations")
    print("  'clear'   - Clear the current chained result or history")
    print("  'exit' or 'quit' - End the program")
    
    while True:
        # Step 1: Handle first number input (including chained calculation check)
        if last_result is not None:
            # We convert to int for presentation if it is a whole number (e.g. 5.0 -> 5)
            display_prev = int(last_result) if last_result.is_integer() else last_result
            print_info(f"Chained result available: {display_prev}")
            num1_input = clean_input(f"Enter first number [or press Enter to use {display_prev}, 'clear' to reset, 'exit']: ")
            
            if num1_input == "":
                num1 = last_result
            elif num1_input.lower() == "clear":
                last_result = None
                print_info("Chained result cleared.")
                continue
            elif num1_input.lower() in ("exit", "quit"):
                break
            elif num1_input.lower() == "history":
                history_manager.display()
                continue
            else:
                # User typed something new, parse it
                try:
                    num1 = parse_number(num1_input)
                except ValueError:
                    print_error(f"'{num1_input}' is not a valid decimal or integer. Please try again.")
                    continue
        else:
            # Normal starting case
            num1_input = clean_input("\nEnter first number (or 'exit'/'history'): ")
            if num1_input.lower() in ("exit", "quit"):
                break
            elif num1_input.lower() == "history":
                history_manager.display()
                continue
            elif num1_input.lower() == "clear":
                history_manager.clear()
                continue
            
            try:
                num1 = parse_number(num1_input)
            except ValueError:
                print_error(f"'{num1_input}' is not a valid decimal or integer. Please try again.")
                continue

        # Step 2: Handle operator input
        op_input = clean_input("Enter operator (+, -, *, /, ÷, %, ^) or 'exit': ")
        if op_input.lower() in ("exit", "quit"):
            break
        elif op_input.lower() == "history":
            history_manager.display()
            continue
        elif op_input.lower() == "clear":
            last_result = None
            print_info("Chained result reset. Starting calculation over.")
            continue
            
        try:
            operator = parse_operator(op_input)
        except ValueError as err:
            print_error(str(err))
            # If we had a chained result, we retain it and let them enter an operator again
            continue

        # Step 3: Handle second number input
        num2_input = clean_input("Enter second number (or 'exit'): ")
        if num2_input.lower() in ("exit", "quit"):
            break
        elif num2_input.lower() == "history":
            history_manager.display()
            continue
        elif num2_input.lower() == "clear":
            last_result = None
            print_info("Chained result reset. Starting calculation over.")
            continue
            
        try:
            num2 = parse_number(num2_input)
        except ValueError:
            print_error(f"'{num2_input}' is not a valid decimal or integer. Please try again.")
            continue

        # Step 4: Perform Dispatch and Logic Execution
        try:
            if operator == "+":
                result = add(num1, num2)
            elif operator == "-":
                result = subtract(num1, num2)
            elif operator == "*":
                result = multiply(num1, num2)
            elif operator == "/":
                result = divide(num1, num2)
            elif operator == "^":
                result = power(num1, num2)
            elif operator == "%":
                result = modulus(num1, num2)
            else:
                # This fallback is a safety catch and should not be reachable under standard parser checks
                print_error(f"Unhandled operation dispatch for operator: {operator}")
                continue

            # Step 5: Format and Print the Result
            # Presentation cleaning for integer values
            n1_print = int(num1) if num1.is_integer() else num1
            n2_print = int(num2) if num2.is_integer() else num2
            res_print = int(result) if result.is_integer() else result
            
            print_success(f"Result: {n1_print} {operator} {n2_print} = {res_print}")
            
            # Step 6: Log in session history and update chained variable
            history_manager.add_entry(num1, operator, num2, result)
            last_result = result
            
        except ZeroDivisionError as err:
            print_error(str(err))
            # Maintain last_result if it existed, otherwise stays None
        except OverflowError:
            print_error("Mathematical overflow. Result is too large for Python float limits.")
        except Exception as e:
            print_error(f"An unexpected mathematical error occurred: {e}")

    print_header("Calculator Shutdown")
    print("Thank you for choosing Gemini Notebook. Good luck with Project 5 submission!")

if __name__ == "__main__":
    run_calculator()
