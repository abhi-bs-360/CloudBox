from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


html = urlopen('http://py4e-data.dr-chuck.net/comments_701312.html', context = ctx).read()
soup = BeautifulSoup(html, "html.parser")

add = 0
tag_type = 'span'

tags = soup(tag_type)
for tag in tags:
    add += int(tag.contents[0])

print("\n")
print(add)
print('\n')
