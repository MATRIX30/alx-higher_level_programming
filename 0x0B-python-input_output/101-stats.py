##!/usr/bin/python3
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


import sys


def print_status():
    '''
        Printing the status of the request
    '''
    counter = 0
    size = 0
    file_size = 0
    status_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
                    "403": 0, "404": 0, "405": 0, "500": 0}

    for lne in sys.stdin:
        line = lne.split()
        try:
            size += int(line[-1])
            code = line[-2]
            status_codes[code] += 1
        except Exception:
            continue
        if counter == 9:
            print("File size: {}".format(size))
            for key, val in sorted(status_codes.items()):
                if (val != 0):
                    print("{}: {}".format(key, val))
            counter = 0
        counter += 1
    if counter < 9:
        print("File size: {}".format(size))
        for key, val in sorted(status_codes.items()):
            if (val != 0):
                print("{}: {}".format(key, val))


if __name__ == "__main__":
    print_status()
