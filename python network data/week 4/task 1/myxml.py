import urllib
import xml.etree.ElementTree as ET

testurl = "http://python-data.dr-chuck.net/comments_197951.xml"

testfile = urllib.urlopen(testurl)
data = testfile.read()
tree = ET.fromstring(data)
vlist = tree.findall('comments/comment')
sum = 0
for item in vlist:
    sum += int(item.find('count').text)
print sum
