import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#Handle SSL Certification Errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#Data Collection
#link = input('Enter URL: ')
#cont = int(input('Enter count: '))
#line = int(input('Enter position: '))

link = 'http://py4e-data.dr-chuck.net/known_by_Danyal.html'
cont = 7
line = 18

print('Retrieving: %s' % link)
for i in range(0, cont):
    html = urllib.request.urlopen(link, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    
    tags = soup('a')
    count = 0
    pos = 0
    for tag in tags:
        pos += 1
        if pos == line:
            print('Retrieving: %s' % str(tag.get('href', None)))
            link = str(tag.get('href', None))
            pos = 0
            break

#Ans
#Name : Kyler