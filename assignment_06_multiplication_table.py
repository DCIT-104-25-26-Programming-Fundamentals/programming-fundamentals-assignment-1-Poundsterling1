# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 6
# Topic: Loops and Functions
# =============================================================================
#
# TASK: Multiplication Table Generator
#
# Write a Python program that generates multiplication tables using loops
# and functions.
#
# -----------------------------------------------------------------------------
# PART A — Single Table
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Print the multiplication table for that number from 1 to 12.
#
# Expected output (if user enters 5):
#
#   Multiplication Table for 5:
#   5  x  1  =  5
#   5  x  2  =  10
#   5  x  3  =  15
#   ...
#   5  x  12 =  60
#
# -----------------------------------------------------------------------------
# PART B — Bonus: Tables from 1 to N
# -----------------------------------------------------------------------------
# - Ask the user to enter a number N.
# - Print the full multiplication table for every number from 1 to N.
# - Add a separator line (e.g. "---") between each table.
#
# Expected output (if user enters 3):
#
#   Multiplication Table for 1:
#   1  x  1  =  1
#   ...
#   1  x  12 =  12
#   ---------------------------
#   Multiplication Table for 2:
#   2  x  1  =  2
#   ...
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - N must be a positive integer. If the user enters an invalid value,
#   print an error message and stop.
# - Each part must be in its own function (see scaffold below).
# - Complete Part A before attempting Part B.
#

## PROGRAMMING FUNDAMENTALS - Assignment 06
# Topic: Loops and Functions
# TASK: Multiplication Table Generator


def print_single_table(num):
    """Generates and prints the multiplication table for a given number from 1 to 12."""
    print(f"Multiplication Table for {num}:")
    for i in range(1, 13):
        print(f"{num} x {i} = {num * i}")


def part_a():
    """Handles Part A: Single Table."""
    print("--- PART A: Single Table ---")
    try:
        num = int(input("Enter a positive integer: "))
        if num <= 0:
            print("Error: Please enter a positive integer.")
            return
        print_single_table(num)
    except ValueError:
        print("Error: Invalid input! Please enter a valid positive integer.")


def part_b():
    """Handles Part B: Tables from 1 to N."""
    print("\n--- PART B: Tables from 1 to N ---")
    try:
        n = int(input("Enter a positive integer N: "))
        if n <= 0:
            print("Error: Please enter a positive integer.")
            return

        for num in range(1, n + 1):
            print_single_table(num)
            if num < n:
                print("---")  # Separator line between tables
    except ValueError:
        print("Error: Invalid input! Please enter a valid positive integer.")


def main():
    part_a()
    part_b()


if __name__ == "__main__":
    main()

