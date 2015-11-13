import re
import urllib
from bs4 import BeautifulSoup

# url = "http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_42.html"
url = "http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_197954.html"
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html, "html.parser")

tags = soup('span')
vlist = []
for tag in tags:
    vlist += re.findall('[0-9]+', tag.string)

sum = 0
for v in vlist:
    sum += int(v)
print sum
