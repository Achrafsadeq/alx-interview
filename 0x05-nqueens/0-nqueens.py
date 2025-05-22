#!/usr/bin/python3
"""N Queens puzzle solver.
Finds all possible arrangements of N queens on an NxN chessboard
where no queens can attack each other.
"""

import sys


def generate_solutions(row, column):
    """Generates all valid queen placements for given board dimensions.
    
    Args:
        row: Number of rows (same as number of queens to place).
        column: Number of columns on the chessboard.
        
    Returns:
        List of all valid queen placement solutions.
    """
    solution = [[]]
    for queen in range(row):
        solution = place_queen(queen, column, solution)
    return solution


def place_queen(queen, column, prev_solution):
    """Places a queen on the board while maintaining safe positions.
    
    Args:
        queen: Current queen to place.
        column: Number of columns to check for placement.
        prev_solution: Solutions from previous placements.
        
    Returns:
        Updated list of valid placements including current queen.
    """
    safe_position = []
    for array in prev_solution:
        for x in range(column):
            if is_safe(queen, x, array):
                safe_position.append(array + [x])
    return safe_position


def is_safe(q, x, array):
    """Checks if a queen can be safely placed at position (q, x).
    
    Args:
        q: Row index to check.
        x: Column index to check.
        array: Current partial solution being evaluated.
        
    Returns:
        True if placement is safe, False otherwise.
    """
    if x in array:
        return False
    return all(abs(array[column] - x) != q - column
              for column in range(q))


def init():
    """Validates and initializes the N value from command line arguments.
    
    Returns:
        Validated integer value of N.
        
    Raises:
        SystemExit: If arguments are invalid.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit():
        n = int(sys.argv[1])
    else:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return n


def n_queens():
    """Main function to solve and print N-Queens puzzle."""
    n = init()
    solutions = generate_solutions(n, n)
    for array in solutions:
        clean = []
        for q, x in enumerate(array):
            clean.append([q, x])
        print(clean)


if __name__ == '__main__':
    n_queens()
