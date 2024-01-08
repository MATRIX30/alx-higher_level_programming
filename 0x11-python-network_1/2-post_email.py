#!/usr/bin/python3
"""
Write a Python script that takes in a URL and an email,
sends a POST request to the passed
URL with the email as a parameter, and displays the body
of the response (decoded in utf-8)

The email must be sent in the email variable
You must use the packages urllib and sys
You are not allowed to import packages other than urllib
and sys
You don’t need to check arguments passed to the script
(number or type)
You must use the with statement
Please test your script in the sandbox provided,
using the web server running on port 5000
"""
if __name__ == "__main__":
    from urllib.request import urlopen, Request
    import sys

    url = sys.argv[1]
    email = sys.argv[2]

    # creating the request and send to url
    sentRequest = Request(url, data={'email': email}, method='POST')

    with urlopen(sentRequest) as response:
        response_body = response.read().decode('utf8')
        print(response_body)
