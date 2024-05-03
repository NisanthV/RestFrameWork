import requests

res=requests.get("http://localhost:8000/api/",params={'abc':123})
print(res.json()['message'])
