import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = input('Enter Address__')
    print(len(address))
    if len(address) < 1:
        break

    url = serviceurl + urllib.parse.urlencode({'address': address})

    print("Retrieving", url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('YOU suck')
        print(data)
        continue
    print(json.dumps(js, indent=4))
    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]['geometry']['location']['lng']
    long_name = js['results'][0]['formatted_address']
    print(long_name)
    print('lat', lat,' lng',lng)
