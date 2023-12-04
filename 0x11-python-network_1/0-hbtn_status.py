#!/usr/bin/python3
"""This module fetches https://alx-intranet.hbtn.io/status"""

if __name__ == "__main__":
    import urllib.request
    import urllib.error
 
    url = "https://alx-intranet.hbtn.io/status"
    try:
        with urllib.request.urlopen(url) as response:
        html = response.read()
        print('Body response:')
        print('\t- type: {}'.format(type(html)))
        print('\t- content: {}'.format(html))
        print('\t- utf8 content: {}'.format(html.decode("utf-8")))
    except urllib.error.URLError as e:
        print(f"Error accessing the URL: {e}")
