#!/usr/bin/python3
"""
UTF-8 Validation Module
This module provides a function to validate if a given list of integers
represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Determines if a given list of integers is a valid UTF-8 encoding.
    """
    num_bytes = 0

    # UTF-8 masks for leading bits
    mask_1_byte = 0b10000000
    mask_2_bytes = 0b11100000
    mask_3_bytes = 0b11110000
    mask_4_bytes = 0b11111000

    for num in data:
        # Ensure the value is within 8 bits
        if num > 255:
            return False

        if num_bytes == 0:
            if (num & mask_1_byte) == 0:
                continue
            elif (num & mask_2_bytes) == 0b11000000:
                num_bytes = 1
            elif (num & mask_3_bytes) == 0b11100000:
                num_bytes = 2
            elif (num & mask_4_bytes) == 0b11110000:
                num_bytes = 3
            else:
                return False
        else:
            if (num & mask_1_byte) != 0b10000000:
                return False
            num_bytes -= 1

    return num_bytes == 0
