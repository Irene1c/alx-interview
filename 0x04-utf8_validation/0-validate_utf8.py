#!/usr/bin/python3
""" UTF-8 Validation """
from typing import List


def validUTF8(data: List[int]) -> bool:
    """ Function that determines if a given data set
        represents a valid UTF-8 encoding
        Each integer represents 1 byte of data therefore,
        handle only the 8 least significant bits of each integer

        Args:
        data: list of integers


        Returns:
        True if data is a valid UTF-8 encoding, else return False

        Example:
        >>> data = [1, 65]
        >>> print(validUTF8(data))
        True

        >>> data = [116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108]
        >>> print(validUTF8(data))
        True

        >>> data = [239, 65, 197, 256]
        >>> print(validUTF8(data))
        False

    """

    try:
        bytes_data = bytes([byte & 0xFF for byte in data])
        bytes_data.decode('utf-8')
        return True
    except UnicodeDecodeError:
        return False


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
