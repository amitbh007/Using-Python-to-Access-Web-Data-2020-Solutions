import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#Handle SSL Certification Errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#Data Collect From the Website
#link = input('Enter - ')
link = 'http://py4e-data.dr-chuck.net/comments_544323.html'
html = urllib.request.urlopen(link, context = ctx).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('span')
sum = 0
count = 0
for tag in tags:
    count += 1
    sum += int(tag.contents[0])

print('Count %d' % count)
print('Sum %d' % sum)

#Ans
#Count 50
#Sum 2833