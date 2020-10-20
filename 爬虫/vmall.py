import requests
from parsel import Selector

url = "https://www.vmall.com/product/10086664213829.html"
resp = requests.get(url)
sel = Selector(resp.text)
res = sel.css("#pro-name::text").extract_first()
print(res)
