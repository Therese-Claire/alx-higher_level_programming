#!/usr/bin/python3
"""Module to take in a URL and sends a POST request to the passed URL"""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email_addr = sys.argv[2]
    values = {
            'email': email_addr
    }

    string_query = urllib.parse.urlencode(values)
    data = string_query.encode('ascii')
    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(req) as response:
        email_response = response.read().decode('utf-8')
        print(email_response)
