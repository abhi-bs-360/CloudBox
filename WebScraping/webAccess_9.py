import json
import urllib.request, urllib.error, urllib.parse
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

random = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_701315.json', context = ctx)
data = random.read().decode()

try:
    js = json.loads(data)
except:
    js = None

add = 0
for item in js["comments"]:
    add += int(item["count"])

print('\nRequired sum :', add, '\n')
