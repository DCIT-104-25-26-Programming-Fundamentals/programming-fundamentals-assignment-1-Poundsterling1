# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# Write a Python program that reads a collection of numbers from the user
# and computes key statistical values using separate functions.
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLE
# -----------------------------------------------------------------------------
#
#   How many numbers? 5
#   Enter number 1: 4
#   Enter number 2: 7
#   Enter number 3: 2
#   Enter number 4: 9
#   Enter number 5: 1
#
#   Results:
#   Sum:     23
#   Average: 4.6
#   Maximum: 9
#   Minimum: 1
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement each calculation in its own function (see scaffold).
# - You may NOT use Python's built-in sum(), max(), or min() functions.
#   Implement the logic yourself using loops inside each function.
# - N must be a positive integer. If the user enters 0 or a negative
#   number, print an error message and stop.
## ==============================================================================
# PROGRAMMING FUNDAMENTALS - Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# ==============================================================================

def calculate_sum(numbers):
    """Calculates the sum of all elements using a loop."""
    total = 0
    for num in numbers:
        total += num
    return total


def calculate_average(numbers):
    """Calculates the average of elements using calculate_sum."""
    if not numbers:
        return 0.0
    return calculate_sum(numbers) / len(numbers)


def calculate_max(numbers):
    """Finds the maximum value using a loop."""
    highest = numbers[0]
    for num in numbers[1:]:
        if num > highest:
            highest = num
    return highest


def calculate_min(numbers):
    """Finds the minimum value using a loop."""
    lowest = numbers[0]
    for num in numbers[1:]:
        if num < lowest:
            lowest = num
    return lowest


def main():
    # Get N from the user
    try:
        n = int(input("How many numbers? "))
    except ValueError:
        print("Error: Invalid input. Please enter an integer.")
        return

    # Requirement: N must be a positive integer
    if n <= 0:
        print("Error: N must be a positive integer.")
        return

    # Collect numbers from the user
    numbers = []
    for i in range(1, n + 1):
        raw_val = input(f"Enter number {i}: ")
        try:
            # Parse as float, then convert to int if it's a whole number
            val = float(raw_val)
            if val.is_integer():
                val = int(val)
            numbers.append(val)
        except ValueError:
            print("Error: Invalid number entered.")
            return

    # Output calculations
    print("\nResults:")
    print(f"Sum:     {calculate_sum(numbers)}")
    print(f"Average: {calculate_average(numbers)}")
    print(f"Maximum: {calculate_max(numbers)}")
    print(f"Minimum: {calculate_min(numbers)}")


if __name__ == "__main__":
    main()

