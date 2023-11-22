#!/usr/bin/python3
"""Given a pile of coins of different values, determine the
    fewest number of coins needed to meet a given amount total
"""
from typing import List


def makeChange(coins: List[int], total: int) -> int:
    """
    Determining the fewest number of coins needed to meet a given amount
    The value of a coin will always be an integer greater than 0

    Args:
    coins (List[int]): A list of coin values
    total (int): The target total amount.

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
    >>> print(makeChange([1, 2, 5], 11))
    3
    >>> print(makeChange([1, 2, 5], 8))
    3
    >>> print(makeChange([2, 4, 6], 10))
    2
    >>> print(makeChange([], 10))
    -1

    """

    if total <= 0:
        return 0

    if coins == []:
        return -1

    num_coins = 0
    coins.sort(reverse=True)

    for val in coins:
        if val <= 0:
            return -1

        num_coins += total // val
        total = total % val
        if total == 0:
            break

    if total == 0:
        return num_coins
    else:
        return -1


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
