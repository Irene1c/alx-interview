#!/usr/bin/python3
""" Module with a function that determines if all the boxes can be opened """


def canUnlockAll(boxes):
    """
    A function that determines if all boxes can be unlocked.
    A key with the same number as a box opens that box
    You can assume all keys will be positive integers

    Args:
        boxes (list of lists): Each list represents a box containing keys
        to other boxes.

    Returns:
        bool: True if all boxes can be unlocked, otherwise False.

    Examples:
        >>> boxes1 = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
        >>> canUnlockAll(boxes1)
        True

        >>> boxes2 = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
        >>> canUnlockAll(boxes2)
        False

        >>> boxes3 = [[1], [2], [3], [4], []]
        >>> canUnlockAll(boxes3)
        True
    """

    n = len(boxes)  # Total number of boxes
    # boolean list to keep track of opened boxes
    unlocked = [False] * n  # initially all set to False
    unlocked[0] = True  # first box is unlocked

    # keep track of boxes that need to be explored
    stack = [0]  # start with box 0

    while stack:
        current_box = stack.pop()  # get box at the top of the stack
        keys = boxes[current_box]  # get the keys in the current box

        for key in keys:
            if key < n and not unlocked[key]:
                unlocked[key] = True
                stack.append(key)  # add box to stack

    # returns True if all boxes can be opened, otherwise False
    return all(unlocked)


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
