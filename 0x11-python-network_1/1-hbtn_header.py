#!/usr/bin/python3
"""
Write a Python script that takes in a URL, sends a request to the URL and
displays
the value of the X-Request-Id variable found in the header of the response.

You must use the packages urllib and sys
You are not allow to import packages other than urllib and sys
The value of this variable is different for each request
You don’t need to check arguments passed to the script (number or type)
You must use a with statement
"""
if __name__ == "__main__":
    from urllib.request import urlopen
    import sys

    url = sys.argv[1]

    with urlopen(url) as response:
        header = response.info()
        request_id = header.get("X-Request-Id")
        print(request_id)
