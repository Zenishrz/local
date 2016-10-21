"""
import time

import requests

request = requests.get("https://google.com")

print(request)

"""

print("Hello")
import requests
newname = requests.get("http://google.com")


if(newname.status_code == 200):
	print("page load sucessfil")
else:
	print("error loading page")