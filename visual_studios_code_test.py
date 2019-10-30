import requests

"""
This comment represents an attempt to better understand the staging/commit
process of git/git-hub. As such, it would be most expedient to ignore it entirely.
"""

r = requests.get("https://coreyms.com")
print(r.status_code)
print(r.ok)