# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#


def read_matrix(rows, cols, name="Matrix"):
    """Read an rows x cols matrix from the user, one row per line."""
    matrix = []
    print(f"\nEnter values for {name} ({rows} x {cols}):")
    for i in range(rows):
        while True:
            raw = input(f"Enter row {i + 1}: ").split()
            if len(raw) != cols:
                print(f"  Error: expected {cols} values, got {len(raw)}. Try again.")
                continue
            try:
                row = [float(x) for x in raw]
            except ValueError:
                print("  Error: please enter numbers only. Try again.")
                continue
            # Store as int if it has no fractional part, for cleaner display
            row = [int(v) if v.is_integer() else v for v in row]
            matrix.append(row)
            break
    return matrix


def print_matrix(matrix, title="Matrix"):
    """Display a matrix in a neat, aligned grid format."""
    print(f"\n{title}:")
    if not matrix:
        print("  (empty)")
        return

    # Find the widest element (as a string) for column alignment
    width = 0
    for row in matrix:
        for value in row:
            width = max(width, len(str(value)))

    for row in matrix:
        line = "  ".join(str(value).rjust(width) for value in row)
        print(" ", line)


# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
def transpose_matrix(matrix):
    """Return the transpose of an M x N matrix as an N x M matrix."""
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0

    # Initialize result matrix with zeros (cols x rows)
    result = [[0 for _ in range(rows)] for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            result[j][i] = matrix[i][j]

    return result


# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
def add_matrices(matrix_a, matrix_b):
    """Return the element-wise sum of two matrices of the same size."""
    rows = len(matrix_a)
    cols = len(matrix_a[0]) if rows > 0 else 0

    result = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            result[i][j] = matrix_a[i][j] + matrix_b[i][j]

    return result


# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
def multiply_matrices(matrix_a, matrix_b):
    """
    Multiply matrix_a (M x N) by matrix_b (N x P) and return the
    result (M x P). Uses three nested loops (i, j, k).
    """
    m = len(matrix_a)
    n = len(matrix_a[0]) if m > 0 else 0
    p = len(matrix_b[0]) if len(matrix_b) > 0 else 0

    result = [[0 for _ in range(p)] for _ in range(m)]

    for i in range(m):          # each row of A
        for j in range(p):      # each column of B
            total = 0
            for k in range(n):  # walk along the shared dimension
                total += matrix_a[i][k] * matrix_b[k][j]
            result[i][j] = total

    return result


# -----------------------------------------------------------------------------
# Helpers for getting valid integer input
# -----------------------------------------------------------------------------
def get_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("  Please enter a positive integer.")
                continue
            return value
        except ValueError:
            print("  Please enter a valid integer.")


# -----------------------------------------------------------------------------
# PART A driver
# -----------------------------------------------------------------------------
def run_transpose():
    print("\n" + "=" * 60)
    print("PART A — TRANSPOSE A MATRIX")
    print("=" * 60)

    rows = get_positive_int("Enter number of rows: ")
    cols = get_positive_int("Enter number of columns: ")

    matrix = read_matrix(rows, cols, "the matrix")
    result = transpose_matrix(matrix)

    print_matrix(matrix, "Original Matrix")
    print_matrix(result, "Transposed Matrix")


# -----------------------------------------------------------------------------
# PART B driver
# -----------------------------------------------------------------------------
def run_addition():
    print("\n" + "=" * 60)
    print("PART B — ADD TWO MATRICES")
    print("=" * 60)

    rows = get_positive_int("Enter number of rows (for both matrices): ")
    cols = get_positive_int("Enter number of columns (for both matrices): ")

    matrix_a = read_matrix(rows, cols, "Matrix A")
    matrix_b = read_matrix(rows, cols, "Matrix B")
    result = add_matrices(matrix_a, matrix_b)

    print_matrix(matrix_a, "Matrix A")
    print_matrix(matrix_b, "Matrix B")
    print_matrix(result, "Sum (A + B)")


# -----------------------------------------------------------------------------
# PART C driver
# -----------------------------------------------------------------------------
def run_multiplication():
    print("\n" + "=" * 60)
    print("PART C — MULTIPLY TWO MATRICES")
    print("=" * 60)

    m = get_positive_int("Enter number of rows for Matrix A (M): ")
    n = get_positive_int("Enter number of columns for Matrix A / rows for Matrix B (N): ")
    p = get_positive_int("Enter number of columns for Matrix B (P): ")

    matrix_a = read_matrix(m, n, "Matrix A")
    matrix_b = read_matrix(n, p, "Matrix B")
    result = multiply_matrices(matrix_a, matrix_b)

    print_matrix(matrix_a, "Matrix A")
    print_matrix(matrix_b, "Matrix B")
    print_matrix(result, "Product (A x B)")


# -----------------------------------------------------------------------------
# MAIN MENU
# -----------------------------------------------------------------------------
def main():
    while True:
        print("\n" + "=" * 60)
        print("MATRIX OPERATIONS MENU")
        print("=" * 60)
        print("1. Transpose a Matrix")
        print("2. Add Two Matrices")
        print("3. Multiply Two Matrices")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            run_transpose()
        elif choice == "2":
            run_addition()
        elif choice == "3":
            run_multiplication()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")


if __name__ == "__main__":
    main()