#!/usr/bin/python3
"""Module to determine the fewest number of coins for a given amount."""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet the total.

    Args:
        coins (list): List of coin denominations.
        total (int): Total amount to reach.

    Returns:
        int: Minimum number of coins needed, or -1 if not possible.
    """
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    coins_used = 0
    for coin in coins:
        if total / coin > 0:
            coins_used = coins_used + (total // coin)
            total = total % coin
        if not total:
            break

    if total != 0 or coins_used == 0:
        return -1
    return coins_used
