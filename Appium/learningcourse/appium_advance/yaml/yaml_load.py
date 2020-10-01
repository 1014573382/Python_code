import yaml
with open(r'./familyInfo.yaml','r') as f:
    data = yaml.load(f, Loader=yaml.FullLoader)

    print(data)
    print(data['name'])
    print(data['spouse'])
    print(data['spouse']['age'])
    print(data['children'][0]['name'])
    print(data['children'][1]['name'])

    data['name'] = 'guoxl'
    print(data['name'])
