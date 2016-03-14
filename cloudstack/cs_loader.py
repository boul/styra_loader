import json
import urllib2
from cs_base_client import BaseClient

api_key = 'your api key'
secret_key = 'your secret key'
url = 'https://cloud/client/api'


client = BaseClient(url, api_key, secret_key)
args = {}
vms = dict()

vms['vms'] = client.request('listVirtualMachines', args)

print json.dumps(vms)

req = urllib2.Request('http://localhost:8081/v1/data/cloudstack')
req.add_header('Content-Type', 'application/json')

response = urllib2.urlopen(req, json.dumps(vms))


print response
