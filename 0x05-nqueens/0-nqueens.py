#!/usr/bin/python3
"""The N queens puzzle.
    Prints every possible solution to the N queens problem
"""
from typing import List


def constraints(board: List[List[str]], row: int, col: int, N: int) -> bool:
    """ Function that ensures the position to place a specific
        Queen on the chessboard is safe
    """

    # check every row in current column
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    # check every column in current row
    for j in range(col):
        if board[row][j] == 'Q':
            return False

    # check diagonal to the left
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    # check diagonal to the right
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 'Q':
            return False

    return True


def solve_puzzle(row: int, position: List[List[int]]) -> None:
    """ Function that solves the N queens problem and
        keeps track of the Queens positions
    """

    N = len(board)

    if row == N:
        pos_copy = position[:]
        results.append(pos_copy)

    for col in range(N):
        if constraints(board, row, col, N):
            board[row][col] = 'Q'
            position.append([row, col])
            solve_puzzle(row + 1, position)
            board[row][col] = '.'
            position.pop()


if __name__ == '__main__':
    from sys import argv, exit

    if len(argv) != 2:
        print('Usage: nqueens N')
        exit(1)
    try:
        N = int(argv[1])
    except ValueError:
        print('N must be a number')
        exit(1)

    if N < 4:
        print('N must be at least 4')
        exit(1)

    # initialization
    results = []
    board = [['.' for _ in range(N)] for _ in range(N)]
    solve_puzzle(0, [])

    for res in results:
        print(res)
