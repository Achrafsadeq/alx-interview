#!/usr/bin/python3
import sys

def backtrack(row, columns, diagonals1, diagonals2, board, N, solutions):
    """
    Recursively place queens on the board using backtracking.
    
    Args:
        row: Current row to place a queen
        columns: Set of occupied columns
        diagonals1: Set of occupied r + c diagonals
        diagonals2: Set of occupied r - c diagonals
        board: List where board[r] is the column of the queen in row r
        N: Size of the board
        solutions: List to store all valid solutions
    """
    if row == N:
        # All queens are placed; add the solution
        solutions.append([[r, board[r]] for r in range(N)])
        return
    
    for col in range(N):
        # Check for conflicts
        if (col not in columns and 
            (row + col) not in diagonals1 and 
            (row - col) not in diagonals2):
            # Place queen
            board[row] = col
            columns.add(col)
            diagonals1.add(row + col)
            diagonals2.add(row - col)
            
            # Recurse to the next row
            backtrack(row + 1, columns, diagonals1, diagonals2, board, N, solutions)
            
            # Backtrack: remove the queen and try the next column
            board[row] = -1
            columns.remove(col)
            diagonals1.remove(row + col)
            diagonals2.remove(row - col)

# Input validation
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

# Initialize data structures
columns = set()          # Occupied columns
diagonals1 = set()       # Occupied r + c diagonals
diagonals2 = set()       # Occupied r - c diagonals
board = [-1] * N         # Board state: board[row] = column
solutions = []           # List of all solutions

# Solve the puzzle
backtrack(0, columns, diagonals1, diagonals2, board, N, solutions)

# Print all solutions
for solution in solutions:
    print(solution)
