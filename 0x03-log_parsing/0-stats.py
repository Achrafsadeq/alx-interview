#!/usr/bin/python3
"""
This script reads from standard input (stdin) line by line
and computes metrics
"""

import sys

status_codes = {
    "200": 0, "301": 0, "400": 0, "401": 0,
    "403": 0, "404": 0, "405": 0, "500": 0
}
total_size = 0
total_lines = 0


def print_stats():
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


try:
    for line in sys.stdin:
        total_lines += 1
        parts = line.split()

        if len(parts) >= 7:
            file_size = parts[-1]
            status_code = parts[-2]

            if file_size.isdigit():
                total_size += int(file_size)

            if status_code in status_codes:
                status_codes[status_code] += 1

        if total_lines % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    print_stats()
    raise


print_stats()
