#!/usr/bin/python3
"""
Write a Python script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8).
"""
import urllib.request
from urllib.error import URLError, HTTPError
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        try:
            response = urlopen(req)
        except HTTPError as e:
            print("Error code: ", e.code)
        else:
            the_page = response.read().decode("utf-8")
