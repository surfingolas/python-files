import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'http://www.dnd5eapi.co/api/monsters'



url = serviceurl

print("Retrieving", url)
uh = urllib.request.urlopen(url)
data = uh.read().decode()
print('retrieved', len(data), 'characters')
try:
    js = json.loads(data)
except:
    js = None

if not js:
    print('YOU suck')
    print(data)

print(json.dumps(js, indent=4))

for stuff in js["results"]:
    print(stuff['name'])
