#!/usr/bin/python3
"""Rotate 2D Matrix """


def rotate_2d_matrix(matrix):
    """
    Given an n x n 2D matrix, rotate it 90 degrees clockwise
    You can assume the matrix will have 2 dimensions and will not be empty

    Args:
    matrix: list of lists

    Returns:
    Does not return anything. The matrix must be edited in-place

    Example:
    >>> matrix = [
    ...     [1, 2, 3, 4],
    ...     [5, 6, 7, 8],
    ...     [9, 10, 11, 12],
    ...     [13, 14, 15, 16]
    ... ]
    >>> rotate_2d_matrix(matrix)
    >>> print(matrix)
    [[13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3], [16, 12, 8, 4]]

    >>> matrix = [
    ...     [1, 2, 3],
    ...     [4, 5, 6],
    ...     [7, 8, 9]
    ... ]
    >>> rotate_2d_matrix(matrix)
    >>> print(matrix)
    [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

    """

    # Transposing (swapping) matrix values
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # Reversing the rows
    for i in range(len(matrix)):
        matrix[i].reverse()


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
