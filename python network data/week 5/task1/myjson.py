import urllib
import json

url = 'http://python-data.dr-chuck.net/comments_197955.json'
handle = urllib.urlopen(url)
data = handle.read()
js = json.loads(data)
sum = 0
for item in js['comments']:
    sum += int(item['count'])
print(sum)
