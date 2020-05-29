import urllib.request,urllib.parse, urllib.error
from bs4 import BeautifulSoup

req_url = input("Enter URL:")
fhand = urllib.request.urlopen('https://'+req_url)
get_html= urllib.request.urlopen('https://'+req_url).read()
soup = BeautifulSoup(get_html,'html.parser')

for line in fhand:
    print(line.decode().strip())

# retrieve all the anchor tag
tags = soup('a')
print("----- Other Links On The Page -----\n")
for tag in tags:
    print(tag.get('href',None))
