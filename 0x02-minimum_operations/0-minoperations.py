#!/usr/bin/python3
""" Module that calculates the fewest number of operations needed
    to result in exactly `n` `H` characters in a file.
    Two operations can be done on the file, Copy All and Paste
"""


def minOperations(n: int) -> int:
    """
    Calculate the minimum number of operations needed to result in
    'n' 'H' characters in a text file using 'Copy All' and 'Paste' operations.

    Args:
    n(int): number for 'H' to result to

    Returns:
    int: minimum number of operations
    If n is impossible to achieve, returns 0

    Examples:
    >>> minOperations(9)
    6
    >>> minOperations(4)
    4
    >>> minOperations(12)
    7

    """

    if n <= 1:
        return 0

    operations = 0
    curr_h = 1
    copy_val = 0  # Variable to hold the copied value

    while curr_h < n:
        if n % curr_h == 0:
            copy_val = curr_h  # Copy All
            curr_h += copy_val  # Paste
            operations += 2  # Count "Copy All" and "Paste" operations
        else:
            curr_h += copy_val  # Paste
            operations += 1  # count "Paste operation"

    return operations


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
