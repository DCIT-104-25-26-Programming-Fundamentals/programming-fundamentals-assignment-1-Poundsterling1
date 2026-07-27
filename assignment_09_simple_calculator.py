# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 9
# =============================================================================
#
# TASK: Console-Based Simple Calculator
#
# Build a calculator program that runs in the console and performs basic
# arithmetic operations based on the user's input.
#
# -----------------------------------------------------------------------------
# OPERATIONS YOUR CALCULATOR MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Addition          ( + )    e.g.  10 + 3  =  13
#   2. Subtraction       ( - )    e.g.  10 - 3  =  7
#   3. Multiplication    ( * )    e.g.  10 * 3  =  30
#   4. Division          ( / )    e.g.  10 / 3  =  3.33
#   5. Modulus           ( % )    e.g.  10 % 3  =  1  (remainder)
#   6. Exponentiation    ( ** )   e.g.  2 ** 8  =  256
#   7. Quit
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ============================
#        SIMPLE CALCULATOR
#   ============================
#   1. Addition
#   2. Subtraction
#   3. Multiplication
#   4. Division
#   5. Modulus
#   6. Exponentiation
#   7. Quit
#   Select an operation (1-7):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Select an operation (1-7): 4
#   Enter first number : 10
#   Enter second number: 3
#   Result: 10 / 3 = 3.33
#
#   Select an operation (1-7): 4
#   Enter first number : 5
#   Enter second number: 0
#   Error: Cannot divide by zero.
#
#   Select an operation (1-7): 7
#   Goodbye!
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Each arithmetic operation MUST be written as its own function.
# - Use a loop so the calculator keeps running until the user selects Quit.
# - Division by zero must be caught and handled with a clear error message
#   (do NOT let the program crash).
# - Division results should be rounded to 2 decimal places.
# - Handle invalid menu choices gracefully.
#

#
## PROGRAMMING FUNDAMENTALS - Assignment 09
# Topic: Functions and Exception Handling
# TASK: Simple Calculator


def add(a, b):
    """Returns the sum of two numbers."""
    return a + b


def subtract(a, b):
    """Returns the difference of two numbers."""
    return a - b


def multiply(a, b):
    """Returns the product of two numbers."""
    return a * b


def divide(a, b):
    """Returns the quotient rounded to 2 decimal places or raises ZeroDivisionError."""
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return round(a / b, 2)


def modulus(a, b):
    """Returns the modulus (remainder) or raises ZeroDivisionError."""
    if b == 0:
        raise ZeroDivisionError("Cannot perform modulus by zero.")
    return a % b


def exponentiate(a, b):
    """Returns a raised to the power of b."""
    return a ** b


def display_menu():
    """Displays the simple calculator menu options."""
    print("\n==============================")
    print("      SIMPLE CALCULATOR       ")
    print("==============================")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Quit")


def get_numbers():
    """Helper function to prompt user for two numeric inputs safely."""
    while True:
        try:
            num1 = float(input("Enter first number : "))
            num2 = float(input("Enter second number: "))
            # Format to int if the number is a whole integer for cleaner output
            num1 = int(num1) if num1.is_integer() else num1
            num2 = int(num2) if num2.is_integer() else num2
            return num1, num2
        except ValueError:
            print("Error: Invalid input! Please enter valid numeric values.")


def main():
    """Main program loop."""
    while True:
        display_menu()
        choice = input("Select an operation (1-7): ").strip()

        if choice == "7":
            print("Goodbye!")
            break

        if choice not in ["1", "2", "3", "4", "5", "6"]:
            print("Error: Invalid choice! Please select an operation from 1 to 7.")
            continue

        num1, num2 = get_numbers()

        try:
            if choice == "1":
                result = add(num1, num2)
                print(f"Result: {num1} + {num2} = {result}")

            elif choice == "2":
                result = subtract(num1, num2)
                print(f"Result: {num1} - {num2} = {result}")

            elif choice == "3":
                result = multiply(num1, num2)
                print(f"Result: {num1} * {num2} = {result}")

            elif choice == "4":
                result = divide(num1, num2)
                print(f"Result: {num1} / {num2} = {result:.2f}" if isinstance(result, float) else f"Result: {num1} / {num2} = {result}")

            elif choice == "5":
                result = modulus(num1, num2)
                print(f"Result: {num1} % {num2} = {result}")

            elif choice == "6":
                result = exponentiate(num1, num2)
                print(f"Result: {num1} ** {num2} = {result}")

        except ZeroDivisionError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main() 

