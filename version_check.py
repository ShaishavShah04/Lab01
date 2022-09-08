import requests as r

# print(r.__version__)

res = r.get("https://raw.githubusercontent.com/ShaishavShah04/Lab01/master/version_check.py")

print(res.text)