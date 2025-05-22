#!/usr/bin/python3
"""
Solves the N Queens puzzle:
Place N non-attacking queens on an N×N chessboard.
"""

import sys


def is_safe(row, col, solution):
    """Check if placing a queen at (row, col) is safe."""
    for r, c in enumerate(solution):
        if c == col or abs(c - col) == row - r:
            return False
    return True


def solve_nqueens(n, row=0, solution=[], solutions=[]):
    """
    Recursively solve the N Queens problem and collect all solutions.
    Each solution is a list of column indices.
    """
    if row == n:
        solutions.append([[r, c] for r, c in enumerate(solution)])
        return

    for col in range(n):
        if is_safe(row, col, solution):
            solve_nqueens(n, row + 1, solution + [col], solutions)


def main():
    """Main entry point: validate input, solve and print all solutions."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)

    n = int(sys.argv[1])

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = []
    solve_nqueens(n, solutions=solutions)

    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
