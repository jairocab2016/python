import requests 

r = requests.get("http://httpbin.org/get")
print(r.status_code)
print(r.status_code == requests.codes.ok)

bad_r = requests.get('http://httpbin.org/status/404')
print(bad_r.status_code)