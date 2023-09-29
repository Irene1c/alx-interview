#!/usr/bin/python3
""" A module that returns a list of lists of integers
    representing the Pascal’s triangle of n.
"""


def pascal_triangle(n):
    """
    A function that returns a list of lists of integers
    representing the Pascal’s triangle of n.

    Args:
        n(int): size/ number of rows to generate

    Returns:
        An empty list if n <= 0
        list of lists of integers representing the Pascal’s triangle

    Example:
        >>> pascal_triangle(5)
        [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

        >>> pascal_triangle(0)
        []

        >>> pascal_triangle(2)
        [[1], [1, 1]]

    """

    triangle = []

    for row in range(n):
        curr_row = []  # initialize current row

        # calculate value of element and append in current row
        for column in range(row + 1):
            if column == 0 or column == row:  # append the leftmost and rightmost 1
                curr_row.append(1)
            else:
                curr_row.append(triangle[row - 1][column - 1] +
                                triangle[row - 1][column])

        triangle.append(curr_row)  # append the current row to the triangle

    return triangle


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
