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


if __name__ == "__main__":
    import sys

    file_size = 0
    st_code = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    counter = 0
    code = 1
    try:
        for line in sys.stdin:
            line_dic = line.split(" ")
            if counter == 10:
                print("File size: {}".format(file_size))
                for key, value in st_code.items():
                    print("{}: {}".format(key, value))
                counter = 1
            code = int(line_dic[-2])
            if code in st_code:
                st_code[code] += 1
            file_size += int(line_dic[-1])
            counter += 1
    except (KeyboardInterrupt, Exception):
        print("File size: {}".format(file_size))
        for key, value in sorted(st_code.items()):
            print("{}: {}".format(key, value))
        raise
