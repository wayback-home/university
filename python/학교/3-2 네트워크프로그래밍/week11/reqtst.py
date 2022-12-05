import requests

res = requests.get("http://210.119.145.6/testsvr")
print(type(res))
print(res.status_code)