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
    continuation_count = 0

    for byte in data:
        if continuation_count == 0:
            if byte >> 5 == 0b110 or byte >> 5 == 0b1110:
                continuation_count = 1
            elif byte >> 4 == 0b1110:
                continuation_count = 2
            elif byte >> 3 == 0b11110:
                continuation_count = 3
            elif byte >> 7 == 0b1:
                return False
        else:
            if byte >> 6 != 0b10:
                return False
            continuation_count -= 1

    return continuation_count == 0
