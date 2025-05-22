#!/usr/bin/python3
"""Solves the N Queens problem"""

import sys


def is_safe(pos, row, col):
    """Check if placing a queen at (row, col) is safe"""
    for r, c in pos:
        if c == col or r - c == row - col or r + c == row + col:
            return False
    return True


def solve_nqueens(N, row=0, pos=[], solutions=[]):
    """Backtracking solver for N Queens"""
    if row == N:
        solutions.append(pos.copy())
        return

    for col in range(N):
        if is_safe(pos, row, col):
            pos.append([row, col])
            solve_nqueens(N, row + 1, pos, solutions)
            pos.pop()


def main():
    """Main function to read input and solve the problem"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = []
    solve_nqueens(N, 0, [], solutions)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
