import requests

r = requests.get('http://github.com', timeout=10)
print(r.cookies)