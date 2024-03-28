#!/usr/bin/python3
"""Module to take in a URL and sends a POST request to the passed URL"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    payload = {
            "email": email
    }
    response = requests.post(url, data=payload)
    print(response.text)
