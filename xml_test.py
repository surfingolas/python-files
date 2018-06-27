from urllib.request import urlopen
import ssl
import xml.etree.ElementTree as ET

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
xml = urlopen(url, context=ctx).read()
stuff = ET.fromstring(xml)
lst = stuff.findall('comment/count')
print(len(lst))
