import json
from urllib2 import urlopen

url= "http://sr-sigmaserv-ad02/api/cms/samehome/by/client/mac/d0e54d2d0739"
r= urlopen(url)

data = json.loads(r.read())

print data [0]["direccion"]

data_string = json.dumps(data)

print data_string