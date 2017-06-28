import requests
from PIL import Image
from StringIO import StringIO
 

r = requests.get("https://github.com/timeline.json")
i = Image.open(StringIO(r.content))