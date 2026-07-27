# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 5
# Topic: Loops, Sequences, and Functions
# =============================================================================
#
# TASK: Fibonacci Sequence Generator
#
# The Fibonacci sequence is a series of numbers where each number is the sum
# of the two numbers before it:
#
#   0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
#
# Write a Python program with TWO parts, each implemented as a function.
#
# -----------------------------------------------------------------------------
# PART A — Print the First N Terms
# -----------------------------------------------------------------------------
# - Ask the user how many terms (N) to display.
# - Print the first N numbers of the Fibonacci sequence on one line.
#
# Example:
#   How many terms? 7
#   Fibonacci sequence: 0 1 1 2 3 5 8
#
# -----------------------------------------------------------------------------
# PART B — Check if a Number Belongs to the Sequence
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Determine whether that number is a Fibonacci number.
# - Print an appropriate message.
#
# Example:
#   Enter a number to check: 13
#   13 is a Fibonacci number.
#
#   Enter a number to check: 20
#   20 is NOT a Fibonacci number.
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use a loop (not recursion) to generate the sequence in both parts.
# - N must be a positive integer. If it is not, print an error message.
# - Each part must be implemented in its own function (see scaffold below).
#

#def generate_fibonacci(n):
# PROGRAMMING FUNDAMENTALS - Assignment 5
# Topic: Fibonacci Sequence
# ==============================================================================

def print_first_n_terms():
    """PART A: Asks for N and prints the first N Fibonacci terms on one line."""
    try:
        n = int(input("How many terms? "))
    except ValueError:
        print("Error: Please enter a valid integer.")
        return

    # Requirement: N must be a positive integer
    if n <= 0:
        print("Error: N must be a positive integer.")
        return

    # Generate the first N terms iteratively
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b

    # Print terms separated by spaces on one line
    print("Fibonacci sequence:", " ".join(map(str, sequence)))


def check_fibonacci_number():
    """PART B: Asks for a number and checks if it belongs to the Fibonacci sequence."""
    try:
        target = int(input("Enter a number to check: "))
    except ValueError:
        print("Error: Please enter a valid integer.")
        return

    if target < 0:
        print(f"{target} is NOT a Fibonacci number.")
        return

    # Loop to generate Fibonacci numbers until reaching or exceeding target
    a, b = 0, 1
    is_fibonacci = False

    while a <= target:
        if a == target:
            is_fibonacci = True
            break
        a, b = b, a + b

    if is_fibonacci:
        print(f"{target} is a Fibonacci number.")
    else:
        print(f"{target} is NOT a Fibonacci number.")


def main():
    print("--- PART A ---")
    print_first_n_terms()
    
    print("\n--- PART B ---")
    check_fibonacci_number()


if __name__ == "__main__":
    main()