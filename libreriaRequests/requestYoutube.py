import requests

url = "https://gdata.youtube.com/feeds/api/videos?q=python&alt=json"
response = requests.get(url)
 
if response.status_code == 200:
   results = response.json()
   for result in results['feed']['entry']:
       print result['title']['$t']
else:
   print "Error code %s" % response.status_code