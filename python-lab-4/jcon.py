import json


file_path = 'sample-data.json'


with open(file_path, 'r') as file:
    data = json.load(file)


print("Interface Status")
print("=" * 80)
print("DN                                                 Description           Speed    MTU")
print("-" * 80)


for item in data['imdata']:
    attributes = item['l1PhysIf']['attributes']
    dn = attributes['dn']
    speed = attributes['speed']
    mtu = attributes['mtu']


    print(f"{dn:<50} {attributes.get('descr', ''):<20} {speed:<8} {mtu}")
