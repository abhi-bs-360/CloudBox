import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

fhandle = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

count = dict()
for line in fhandle:
    dummy = line.decode().strip()
    print(dummy)

    for i in dummy.split():
        count[i] = count.get(i, 0) + 1

print("\n", count)
