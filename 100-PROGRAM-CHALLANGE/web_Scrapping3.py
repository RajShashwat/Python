import urllib
import xml.etree.ElementTree as ET

url = input("Enter location: ")

xml = urllib.request.urlopen(url).read()

tree = ET.fromstring(xml)

counts =  tree.findall('.//count')

accumulator = 0

for count in counts:
    accumulator += int(count.text)

print ("Sum:" + str(accumulator))