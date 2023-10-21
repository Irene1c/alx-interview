#!/usr/bin/python3
""" script that reads stdin line by line and computes metrics"""
import sys


status_codes = (200, 301, 400, 401, 403, 404, 405, 500)


def print_stats(lines):
    """
    Function that reads stdin line by line and computes metrics

    Args:
    lines(str): lines representing the stdin

    Returns:
    After every 10 lines and/or a keyboard interruption (CTRL + C),
    prints the following statistics:
        Total file size: File size: <total size>
        Number of lines by status code: <status code>: <number>
        status codes should be printed in ascending order

    """

    line_count = 1
    status_count = 0
    total_size = []
    all_status_codes = []
    try:
        for line in lines:
            parts = line.split(" ")

            if len(parts) != 9:
                continue

            file_size = parts[-1]
            total_size.append(int(file_size))
            status_code = parts[-2]
            all_status_codes.append(int(status_code))
            if line_count % 10 == 0:
                print("File size:", sum(total_size))
                for i in status_codes:
                    status_count = all_status_codes.count(i)
                    if status_count > 0:
                        print("{:d}: {:d}".format(i, status_count))
            line_count += 1
    finally:
        print("File size:", sum(total_size))
        for i in status_codes:
            status_count = all_status_codes.count(i)
            if status_count > 0:
                print("{:d}: {:d}".format(i, status_count))


print_stats(sys.stdin)
