import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'https://raw.githubusercontent.com/adrpadua/5e-database/master/5e-SRD-Ability-Scores.json'



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


print(js[0]['desc'])
