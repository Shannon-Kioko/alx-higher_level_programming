#!usr/bin/python3
"""
101-stats module
This script reads stdin line by line and computes metrics based on the
provided input format.
The input format is as follows:
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>

Metrics Computed:
- Total file size: The sum of file sizes encountered since the beginning.
- Number of lines by status code: The count of different status codes
encountered, grouped by status code.

Possible status codes: 200, 301, 400, 401, 403, 404, 405, and 500.

The script prints the computed metrics every 10 lines of input or
when a keyboard interruption (CTRL + C) occurs.
"""


import sys
from collections import defaultdict

def print_metrics(total_size, status_count):
  """
    Print the computed metrics.

    Args:
        total_size (int): The total file size computed so far.
        status_count (dict): A dictionary containing the counts of different
        status codes encountered.

    Returns:
        None
    """
    print(f"Total file size: {total_size}")
    for status_code in sorted(status_count.keys()):
        print(f"{status_code}: {status_count[status_code]}")

def parse_line(line):
  """
    Parse a line of input and extract the status code and file size.

    Args:
        line (str): A line of input in the specified format.

    Returns:
        tuple or None: A tuple containing the status code and file size if
        successfully parsed,
                       otherwise, returns (None, None).
    """
    try:
        _, _, _, status_code, file_size = line.strip().split(" ")
        return int(status_code), int(file_size)
    except ValueError:
        return None, None

def main():

     """
    Read standard input (stdin) line by line and compute metrics.

    Returns:
        None
    """
    total_size = 0
    status_count = defaultdict(int)
    line_count = 0

    try:
        for line in sys.stdin:
            status_code, file_size = parse_line(line)
            if status_code is not None and file_size is not None:
                total_size += file_size
                status_count[status_code] += 1
                line_count += 1

            if line_count == 10:
                print_metrics(total_size, status_count)
                line_count = 0

    except KeyboardInterrupt:
        print_metrics(total_size, status_count)
