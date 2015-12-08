import urllib
import json

serviceurl = 'http://python-data.dr-chuck.net/geojson?'
url = serviceurl + urllib.urlencode({'sensor':'false', 'address':'University of West Florida'})
#print(url)

handle = urllib.urlopen(url)
data = handle.read()
js = json.loads(data)
#print(json.dumps(js, indent = 4))
print(js['results'][0]['place_id'])
