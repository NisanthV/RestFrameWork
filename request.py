import requests

res=requests.post("http://localhost:8000/api/",json={'title':'abc','content':"this is trying for post method"})
print(res.json())
