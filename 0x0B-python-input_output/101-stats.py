#!/usr/bin/python3

def print_stats(size, status_codes):
    """
    Print statistics including file size and HTTP status codes.

    Args:
        size (int): The total file size.
        status_codes (dict): A dictionary containing HTTP status codes and their counts.

    Returns:
        None
    """
    print("File size: {}".format(size))
    for key in sorted(status_codes):
        print("{}: {}".format(key, status_codes[key]))

if __name__ == "__main__":
    import sys

    size = 0
    status_codes = {}
    valid_codes = {'200', '301', '400', '401', '403', '404', '405', '500'}
    count = 0

    try:
        for current_line in sys.stdin:
            if count == 10:
                print_stats(size, status_codes)
                count = 1
            else:
                count += 1

            line_parts = current_line.split()

            try:
                size += int(line_parts[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line_parts[-2] in valid_codes:
                    status_codes[line_parts[-2]] = status_codes.get(line_parts[-2], 0) + 1
            except IndexError:
                pass

        print_stats(size, status_codes)

    except KeyboardInterrupt:
        print_stats(size, status_codes)
        raise
