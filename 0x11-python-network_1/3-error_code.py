#!/usr/bin/python3
"""
Write a Python script that takes in a URL, sends a request
to the URL and displays the body of the response
(decoded in utf-8).

You have to manage urllib.error.HTTPError exceptions
and print: Error code: followed by the HTTP status code
You must use the packages urllib and sys
You are not allowed to import other packages than urllib
and sys
You don’t need to check arguments passed to the script
(number or type)
You must use the with statement
"""

if __name__ == "__main__":
    from urllib.request import urlopen
    import urllib
    import sys

    url = sys.argv[1]

    try:
        with urlopen(url) as response:
            data = response.read()
            data_decoded = data.decode('utf-8')
            print(data_decoded)

    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
