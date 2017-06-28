import requests 

r = requests.get("http://httpbin.org/get")
print(r.headers)
print(r.headers["content-type"])
print(r.headers["connection"])
print(r.headers.get("content-type"))