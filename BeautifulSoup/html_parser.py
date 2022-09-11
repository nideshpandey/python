from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
# Input URL by the user
url = input('Enter - ')

# Opens the url and read the HTML content
html = urlopen(url, context=ctx).read()

# sou object consists the parsed HTML
soup = BeautifulSoup(html, "html.parser")

span_list = list()

# Retrieve all of the span tags
span_tags = soup('span')
for tag in span_tags:
    # print('Contents:', tag.contents[0])
    # span_list.append(int(tag.contents[0]))

    # Obtain the content of the span tag
    span_list.append(tag.contents[0])

# print(span_list)

# Map string to numbers INT
new_span_list = list(map(int, span_list))

total = sum(new_span_list)

print(total)
