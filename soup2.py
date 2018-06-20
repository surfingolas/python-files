

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
urllist = list()
count = int(input("Enter count: "))
pos = int(input("Enter Pos: "))
newurl = None

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    yes = tag.get('href', None)
    #create a list of all the urls on this page
    urllist.append(yes)
# change the url to match the input from the url list
for i in range(count):
    newurl = urllist[pos - 1]
    html2 = urllib.request.urlopen(newurl, context=ctx).read()
    soup2 = BeautifulSoup(html2, 'html.parser')
    urllist = list()
    tags2 = soup2('a')
    for everything in tags2:
        stop = everything.get('href', None)
        urllist.append(stop)
itsanice = newurl.split("_")
namelist = list(itsanice[2])
finito = ''.join(namelist[:-5])
print(finito)
