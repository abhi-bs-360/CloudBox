import json
import urllib.request, urllib.parse, urllib.error
import ssl

api_key = False

if api_key is False:
    api_key = 42
    service_url = 'http://py4e-data.dr-chuck.net/json?'
else:
    service_url = 'https://maps.googleapis.com/maps/api/geocode/json?'


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


for chance in range(1):
    address = 'SASTRA University'
    if len(address) < 1:
        break

    parms = dict()
    parms['address'] = address
    if api_key is not False:
        parms['key'] = api_key
    url = service_url + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    random = urllib.request.urlopen(url, context = ctx)
    data = random.read().decode()
    print(len(data))

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print("===Failure_to_Retrieve===")
        print(data)
        continue

    print(json.dumps(js, indent = 4))

    answer = js['results'][0]['place_id']
    print(answer)
