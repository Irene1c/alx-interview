#!/usr/bin/python3
""" script that reads stdin line by line and computes metrics"""
import re
import sys


# if the format is not this one, the line must be skipped
input_format = r'^' \
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - ' \
    r'\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6}\] ' \
    r'"GET /projects/260 HTTP/1.1" (\d{3}) (\d+)$'

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
            if not re.match(input_format, line):
                continue

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
