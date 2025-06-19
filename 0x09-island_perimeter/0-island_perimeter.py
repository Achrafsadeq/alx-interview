#!/usr/bin/python3
"""
This module contains the island_perimeter function.
"""

def island_perimeter(grid):
    """
    Returns the perimeter of the island described in the grid.
    """
    perimeter = 0
    height = len(grid)
    width = len(grid[0]) if height > 0 else 0

    for i in range(height):
        for j in range(width):
            if grid[i][j] == 1:
                perimeter += 4
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2
    return perimeter
