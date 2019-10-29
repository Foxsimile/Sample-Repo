import requests

r = requests.get("https://corems.com")
print(r.status.code)
print(r.ok)