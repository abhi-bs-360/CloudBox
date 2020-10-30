from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


html = urlopen('http://py4e-data.dr-chuck.net/known_by_Raunaq.html', context = ctx).read()
soup = BeautifulSoup(html, "html.parser")


for i in range(7):

    tag_type = 'a'
    tags = soup(tag_type)

    count = 1
    for tag in tags:

        if count <= 18:
            dummy = tag.get('href', None)
            count += 1

        else:
            html = urlopen(dummy, context = ctx).read()
            soup = BeautifulSoup(html, "html.parser")
            break

    temp = (dummy).split('_')
    print((temp[2])[0:-5])
