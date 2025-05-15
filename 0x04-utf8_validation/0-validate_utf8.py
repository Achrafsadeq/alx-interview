#!/usr/bin/python3
"""
UTF-8 Validation Module
This module provides a function to validate if a given list of integers
represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Determines if a given list of integers is a valid UTF-8 encoding.

    Args:
        data (list): A list of integers representing byte values.

    Returns:
        bool: True if data is a valid UTF-8 encoding, False otherwise.
    """
    num_bytes = 0

    for i in data:
        if num_bytes == 0:
            if i >> 5 == 0b110 or i >> 5 == 0b1110:
                num_bytes = 1
            elif i >> 4 == 0b1110:
                num_bytes = 2
            elif i >> 3 == 0b11110:
                num_bytes = 3
            elif i >> 7 == 0b0:
                continue
            else:
                return False
        else:
            if i >> 6 != 0b10:
                return False
            num_bytes -= 1

    return num_bytes == 0
