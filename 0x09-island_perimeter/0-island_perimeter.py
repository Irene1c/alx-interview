#!/usr/bin/python3
"""Island Perimeter"""


def island_perimeter(grid) -> int:
    """
    Function that returns the perimeter of the island described in grid

    Args:
    grid (List of lists of integers) : grid is rectangular
                               0 represents water
                               1 represents land
                                Each cell is square, with a side length of 1
                                Cells are connected horizontally/vertically

    Returns:
    perimeter (int) of island described in the grid

    Example:
    >>> grid = [[0],[0],[0]]
    >>> print(island_perimeter(grid))
    0
    >>> grid = [[1, 1, 1, 1, 1],[1, 1, 1, 1, 1],[1, 1, 1, 1, 1]]
    >>> print(island_perimeter(grid))
    16
    >>> grid = [[1, 1, 1, 0, 0, 0],[0, 1, 1, 1, 0, 0],[0, 0, 0, 1, 1, 1]]
    >>> print(island_perimeter(grid))
    18
    >>> grid = [[0, 1, 1, 0, 0, 0],[0, 1, 1, 1, 0, 0],[0, 0, 0, 0, 0, 0]]
    >>> print(island_perimeter(grid))
    10

    """

    perimeter = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1
                if j == len(grid[i]) - 1 or grid[i][j + 1] == 0:
                    perimeter += 1
                if i == len(grid) - 1 or grid[i + 1][j] == 0:
                    perimeter += 1
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1

    return perimeter


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
