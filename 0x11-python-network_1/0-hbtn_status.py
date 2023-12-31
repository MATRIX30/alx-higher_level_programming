#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status

You must use the package urllib
You are not allowed to import any packages other than urllib
The body of the response must be displayed like the following
example (tabulation before -)
You must use a with statement
"""

if __name__ == "__main__":
    from urllib.request import urlopen

    url = "https://alx-intranet.hbtn.io/status"

    with urlopen(url) as response:
        data = response.read()
        data_decoded = data.decode('utf-8')

        # display data
        print("Body response:")
        print("\t- type: {}".format(type(data)))
        print("\t- content: {}".format(data))
        print("\t- utf8 content: {}".format(data_decoded))
