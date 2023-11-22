#!/usr/bin/python3
"""Given a pile of coins of different values, determine the
    fewest number of coins needed to meet a given amount total
"""
from typing import List


def makeChange(coins: List[int], total: int):
    """
    Determining the fewest number of coins needed to meet a given amount
    The value of a coin will always be an integer greater than 0

    Args:
    coins: list
    total: int

    Returns:
    If total is 0 or less, return 0
    If total cannot be met by any number of coins you have, return -1
    Fewer number of coins needed to meet `total`

    Example:
    >>> print(makeChange([1, 2, 25], 37))
    7
    >>> print(makeChange([1256, 54, 48, 16, 102], 1453))
    -1
    >>> print(makeChange([1, 2, 3], -4))
    0

    """

    num = 0
    n = len(coins) - 1
    coins.sort(reverse=True)

    if total <= 0:
        return 0

    for i in coins:
        if total % i == 0:
            num += total // i
            break
        else:
            total = total - i
            if total < 0:
                return -1
            elif i == coins[n] and total != 0:
                return -1
            num += 1

    return num


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
