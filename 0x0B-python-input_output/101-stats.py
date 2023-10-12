#!/usr/bin/python3
"""Script that reads stdin line by line and computes metrics:
- Input format: <IP Address> - [<date>] "GET /projects/260
  HTTP/1.1" <status code> <file size>
- Each 10 lines and after a keyboard interruption (CTRL + C),
prints those statistics since the beginning:
    - Total file size: File size: <total size>
    - where is the sum of all previous (see input format above)
    - Number of lines by status code:
        * possible status code: 200, 301, 400, 401, 403, 404,
          405 and 500
        * if a status code doesn’t appear, don’t print anything
          for this status code
        * format: <status code>: <number>
        * status codes should be printed in ascending order

"""


def print_data(file_size: int, status_code: dict) -> None:
    """method to print log data"""
    print("File size: {}".format(file_size))
    for key, value in sorted(status_code.items()):
        if value != 0:
            print("{}: {}".format(key, value))


if __name__ == "__main__":
    import sys

    file_size = 0
    status_code = {200: 0, 301: 0, 400: 0, 401: 0,
                   403: 0, 404: 0, 405: 0, 500: 0}
    counter = 0

    try:
        for line in sys.stdin:
            line_lst = line.split(" ")
            if counter == 10:
                print_data(file_size, status_code)
                counter = 0
            try:
                file_size += int(line_lst[-1])
                code = int(line_lst[-2])
                if code in status_code:
                    status_code[code] += 1

            except Exception:
                pass
            counter += 1

        print_data(file_size, status_code)
    except KeyboardInterrupt:
        print_data(file_size, status_code)
        raise
