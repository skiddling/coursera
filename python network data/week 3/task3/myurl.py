from bs4 import BeautifulSoup
import urllib

myfile = urllib.urlopen('https://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Azlan.html')
html = BeautifulSoup(myfile,"html.parser")
hrefs = html.find_all('a')
href = hrefs[17]

for i in range(0, 6):
     myfile = urllib.urlopen(href.get('href'))
     html = BeautifulSoup(myfile, "html.parser")
     hrefs = html.find_all('a')
     href = hrefs[17]

print(href.get_text())
