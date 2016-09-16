#!/usr/bin/python

import argparse
import urllib2
import json
import ssl

parser = argparse.ArgumentParser()
parser.add_argument("--username")
parser.add_argument("--password")
parser.add_argument("--k8s-url", help="https://api.kubernetes.io")
parser.add_argument("--styra-url", help="https://styra.com")
args = parser.parse_args()

if hasattr(ssl, '_create_unverified_context'):
    ssl._create_default_https_context = ssl._create_unverified_context

username = args.username
password = args.password
url = args.k8s_url
styra_url = args.styra_url

passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
passman.add_password(None, url, username, password)
authhandler = urllib2.HTTPBasicAuthHandler(passman)
opener = urllib2.build_opener(authhandler)
urllib2.install_opener(opener)

data = dict()

response = urllib2.urlopen(url + '/api/v1/nodes')
data['nodes'] = json.load(response)['items']

response = urllib2.urlopen(url + '/api/v1/pods')
data['pods'] = json.load(response)['items']

response = urllib2.urlopen(url + '/api/v1/services')
data['services'] = json.load(response)['items']

response = urllib2.urlopen(url + '/apis/extensions/v1beta1/deployments')
data['deployments'] = json.load(response)['items']

response = urllib2.urlopen(url + '/apis/extensions/v1beta1/ingresses')
data['ingresses'] = json.load(response)['items']

response = urllib2.urlopen(url + '/apis/extensions/v1beta1/replicasets')
data['replicasets'] = json.load(response)['items']

print data
req = urllib2.Request(styra_url + '/v1/data/kubernetes')
req.add_header('Content-Type', 'application/json')

response = urllib2.urlopen(req, json.dumps(data))