# -*- coding: utf-8 -*-
import requests

#r = requests.get('https://github.com/timeline.json') #objeto response llamado r
#r = requests.post("http://httpbin.org/post") #petición HTTP POST
# r = requests.put("http://httpbin.org/put")
# r = requests.delete("http://httpbin.org/delete")
r = requests.head('http://httpbin.org/get')
#r = requests.options("http://httpbin.org/get")
print(r.status_code)