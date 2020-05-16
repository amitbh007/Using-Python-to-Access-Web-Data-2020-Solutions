import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False
# If you have a Google Places API key, enter it here

if api_key is False:
    api_key = 42
    #DO NOT USE /geojson? ENDPOINT
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#address = input('Enter location: ')
address = 'UIUC'

parms = dict()
parms['address'] = address
if api_key is not False: parms['key'] = api_key
url = serviceurl + urllib.parse.urlencode(parms)

#final encoded URL will be
#http://py4e-data.dr-chuck.net/json?key=42&address=UIUC

print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

js = json.loads(data)

if not js or 'status' not in js or js['status'] != 'OK':
    print('==== Failure To Retrieve ====')

pid = js['results'][0]['place_id']
print('place_id:', pid)

#Ans
#place_id :  ChIJ6VUmqSTXDIgR-iZoBCUFPKU