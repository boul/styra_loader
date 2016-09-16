#!/usr/bin/python

import json
import urllib2
import argparse
from cs_base_client import BaseClient

parser = argparse.ArgumentParser()
parser.add_argument("--api-key")
parser.add_argument("--secret-key")
parser.add_argument("--cs-url", help="https://cloudstack.com/client/api")
parser.add_argument("--styra-url", help="https://styra.com")
args = parser.parse_args()


url = args.cs_url
api_key = args.api_key
secret_key = args.secret_key
styra_url = args.styra_url

client = BaseClient(url, api_key, secret_key)
args = {}
data = dict()

data['virtualmachines'] = client.request('listVirtualMachines', args)
data['networks'] = client.request('listNetworks', args)
data['vpcs']  = client.request('listVPCs', args)
# data['loadbalancers'] = client.request('listLoadBalancers', args)
data['loadbalancerrules'] = client.request('listLoadBalancerRules', args)
data['portforwardingrules'] = client.request('listPortForwardingRules', args)
print json.dumps(data)

req = urllib2.Request(styra_url + '/v1/data/cloudstack')
req.add_header('Content-Type', 'application/json')

response = urllib2.urlopen(req, json.dumps(data))


print response
