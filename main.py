from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
cert = ssl.create_default_context()
cert.check_hostname = False
cert.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=cert).read()
soup = BeautifulSoup(html, "html.parser")
print(soup)

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    # Look at the parts of a tag
    print('TAG:', tag)
    print('URL:', tag.get('href', None))
    print('Contents:', tag.contents[0])
    print('Attrs:', tag.attrs)
