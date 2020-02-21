import urllib
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('URL:  ')
position = int(input("Position: "))-1
count = int(input("Count: "))
soup = BeautifulSoup(urllib.request.urlopen(url, context=ctx).read(), 'html.parser')
Sequence = []
tags = soup('a')
for i in range(count):
    link = tags[position].get('href', None)
    print("Retrieving:",link)
    Sequence.append(tags[position].contents[0])
    soup = BeautifulSoup(urllib.request.urlopen(link, context=ctx).read(), 'html.parser')
    tags = soup('a')
    link = tags[position].get('href', None)
print(Sequence[-1])