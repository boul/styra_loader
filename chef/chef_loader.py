
import chef
import json
import pprint
import urllib2

bla = chef.autoconfigure()

# client = bla.client

nodes = chef.Node.list()

d = dict()
summ = []

for node in nodes:
    print node

    ohai = chef.Node(node).automatic.to_dict()
    summ.append(ohai)

    d['nodes'] = summ


json_output = json.dumps(d)
print json_output

req = urllib2.Request('https://styra.boul.nl/v1/data/ohai')
req.add_header('Content-Type', 'application/json')

response = urllib2.urlopen(req, json_output)

print response


