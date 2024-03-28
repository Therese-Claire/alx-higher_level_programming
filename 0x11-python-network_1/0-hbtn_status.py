#!/usr/bin/python3
"Module that fetches https://alx-intranet.hbtn.io/status"
import urllib.request



if __name__ == "__main__":
    url = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(url) as response:
        res_page = response.read()
        print('Body response:')
        print('\t- type: {}'.format(type(res_page)))
        print('\t- content: {}'.format(res_page))
        print('\t- utf8 content: {}'.format(res_page.decode("utf-8")))

