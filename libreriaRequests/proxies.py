import requests

proxies = {
  "http": "http://10.10.1.10:3128",
  "https": "http://10.10.1.10:1080",
}

#proxie propio
# proxies = {
#     "http": "http://user:pass@10.10.1.10:3128/",
# }

r = requests.get("http://example.org", proxies=proxies)