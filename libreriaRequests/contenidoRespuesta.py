# -*- coding: utf-8 -*-
import requests

r = requests.get("https://github.com/timeline.json")
print(r.encoding) #conocer codificacion
r.encoding = 'ISO-8859-1' #cambiar codificacion
print(r.encoding)
print(type(r.content))