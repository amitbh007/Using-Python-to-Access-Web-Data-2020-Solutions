import urllib.request, urllib.parse, urllib.error
import json

#Data collection
#link = input('Enter location: ')
link = 'http://py4e-data.dr-chuck.net/comments_544326.json'
print('Retrieving', link)

html = urllib.request.urlopen(link).read().decode()
print('Retrieved', len(html), 'characters')

js = json.loads(html)

count = 0
sum = 0
for item in js['comments']:
    count += 1
    sum += int(item['count'])

print('Count:', count)
print('Sum:', sum)

#Ans
#Retrieved 2725 characters
#Count: 50
#Sum: 2530