import requests as r

# print(r.__version__)

res = r.get("https://raw.githubusercontent.com/ShaishavShah04/Crypto-Scanner/main/scanner.py")

print(res.text)