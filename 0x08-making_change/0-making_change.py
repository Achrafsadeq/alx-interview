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

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for x in range(coin, total + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
