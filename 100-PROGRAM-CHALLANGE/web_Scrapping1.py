import urllib
from bs4 import BeautifulSoup

soup = BeautifulSoup(urllib.request.urlopen(input("URL: ")), "html.parser")

spans = soup('span')

num = []

for span in spans:
    num.append(int(span.string))

print (sum(num))