#!/usr/bin/python3
"""
Pascal's Triangle
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing Pascal’s triangle of n
    """
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        if i == 0:
            triangle.append([1])
        else:
            prev = triangle[-1]
            new_row = [1]
            for j in range(1, len(prev)):
                new_row.append(prev[j - 1] + prev[j])
            new_row.append(1)
            triangle.append(new_row)

    return triangle
