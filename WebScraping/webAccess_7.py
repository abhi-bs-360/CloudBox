import json

data = '''[ { "id": "001", "x": "98", "name": "Abhiram"}, { "id": "007", "x": "72", "name": "Chuck"} ]'''

tree = json.loads(data)
print("User count:", len(tree))

for item in tree:
    print('Name :', item['name'])
    print('Id :', item['id'])
    print('Attr :', item['x'])
    print('\n')
