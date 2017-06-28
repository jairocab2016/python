import requests

s = requests.Session()
s.auth = ('user', 'pass')
s.headers.update({'x-test': 'true'})

# se envian ambos: 'x-test' y 'x-test2'
s.get('http://httpbin.org/headers', headers={'x-test2': 'true'})

print (s.headers)