import json
import urllib
count = 0

url = input("URL: ")
print ("retrieving URL. Stand by.")
data = urllib.request.urlopen(url).read()

info = json.loads(data)
for item in info["comments"]:
	number = int(item["count"])
	count = count + number
print (count)