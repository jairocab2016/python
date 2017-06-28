import requests
import json

url = 'https://api.github.com/some/endpoint'
payload = {'some':'data'}
headers = {'content-type': 'application/json'}

r = requests.post(url, data = json.dumps(payload), headers = headers)

print(r.json())
print(r.url)