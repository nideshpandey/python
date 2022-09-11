"""
Follows a url link for certain counts as specified to obatin the content of a certain anchor tag at certain position.
"""

import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
count = int(input("Enter count: "))
position = int(input('Enter position: '))


def ObtainUrl(url):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    return soup

# Retrieve all of the anchor tags


all_tags = list()

for i in range(count):
    soup = ObtainUrl(url)
    print('Retrieving:', url)
    tags = soup('a')
    for tag in tags:
        if tag == tags[position]:

            # print(tag.get('href', None))
            all_tags.append(tag.contents[0])
            url = tag.get('href', None)


print(all_tags[-1])
