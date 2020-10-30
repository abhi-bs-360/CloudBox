import xml.etree.ElementTree as ET
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

random = urlopen('http://py4e-data.dr-chuck.net/comments_701314.xml', context = ctx)
data = random.read()
print('Retrieved', len(data), 'characters')

trees = ET.fromstring(data)
lists = trees.findall('comments/comment')

add = 0
for item in lists:
    add += int(item.find('count').text)

print("Required_Sum :", add)
