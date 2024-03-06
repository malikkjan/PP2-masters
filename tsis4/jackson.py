import json


with open('sample-data.json', 'r') as file:
    data = json.load(file)


headers = ["DN", "Description", "Speed", "MTU"]


print("{:<50} {:<20} {:<8} {:<8}".format(*headers))
print("-" * 100)


for entry in data:
    dn = entry['l1PhysIf']['attributes']['dn']
    description = entry['l1PhysIf']['attributes']['descr']
    speed = entry['l1PhysIf']['attributes']['speed']
    mtu = entry['l1PhysIf']['attributes']['mtu']


    print("{:<50} {:<20} {:<8} {:<8}".format(dn, description, speed, mtu))
