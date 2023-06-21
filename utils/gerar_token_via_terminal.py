import requests


url = "http://localhost:8000/api/v1/token/login/"
payload = {"email": "salomao1@gmail.com", "password": "mudar123"}
headers = {"Content-Type": "application/json"}
response = requests.request("POST", url, json=payload, headers=headers)
print(response.json())
