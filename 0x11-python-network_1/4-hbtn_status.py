#!/usr/bin/python3
"Module that fetches https://alx-intranet.hbtn.io/status"
import requests


if __name__ == "__main__":
    res_page = requests.get("https://alx-intranet.hbtn.io/status")
    content = res_page.text
    print('Body response:')
    print('\t- type: {}'.format(type(content)))
    print('\t- content: {}'.format(content))
