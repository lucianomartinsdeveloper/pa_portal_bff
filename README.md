# **Projeto Backend para o Pipoca Ágil**

# Para começar
* Crie um virtualenv com Python.

#### Windows

``python -m venv .venv``

#### Linux

``python3 -m venv .venv``

* Ative o virtualenv.
#### Windows
`` .venv/Scripts/activate``

#### Linux
`` source .venv/bin/activate``

OBS: À partir de agora que acessou a virtualenv todos os comandos dentro dela só precisa usar **python e pip**

* Instale as dependências.

``pip install -r requirements\dev.txt``

* Gerar o arquivo o *.env*

``python contrib/env_gen.py``

* Fazer as alterações necessárias

* Rode as migrações.

```python manage.py migrate```

* Criar um usuário padrão

``python manage.py createsuperuser``

* Rode a aplicação

``python manage.py runserver``

### Dados esperados do frontend:
* _**Nome**_
* **_Data de Nascimento no formato (YYYY-MM-DD)_**
* **_Tipos de público_**
* **_Senha de pelo menos 8 caracteres não permitido repetidos_**

## Salvar dados no Sistema (Endpoints)

* Adicionar Usuário
````
import requests
url = "http://localhost:8000/api/v1/users/"
payload = {
    "username": "Salomão Garu da Silva",
    "email": "salomao1@gmail.com",
    "password": "mudar123",
    "birth_date": "2003-06-20",
    "type_of_audience": "PRO"
}
headers = {"Content-Type": "application/json"}
response = requests.request("POST", url, json=payload, headers=headers)
print(response.text)
````

* Fazer o login para gerar o token
````
import requests
url = "http://localhost:8000/api/v1/token/login/"
payload = {
    "email": "salomao1@gmail.com",
    "password": "mudar123"
}
headers = {"Content-Type": "application/json"}
response = requests.request("POST", url, json=payload, headers=headers)
token = response.json()

print(token)
{
	"auth_token": "aa4e39aeb7f7442442e0d532640ca6bf5eac7764"
}
````

* Listar informações do usuário
````
import requests
url = "http://localhost:8000/api/v1/users/"
payload = ""
headers = {"Authorization": "Token 8c63871746b65f809124a21a0b4fe6e7edfc0340"}
response = requests.request("GET", url, data=payload, headers=headers)
print(response.text)
[
	{
		"username": "Salomão Garu da Silva",
		"birth_date": "2003-06-20",
		"id": 3,
		"email": "salomao1@gmail.com"
	}
]
````

* Faz logout e apaga o token

````
import requests
url = "http://localhost:8000/api/v1/token/logout/"
payload = ""
headers = {"Authorization": "Token aa4e39aeb7f7442442e0d532640ca6bf5eac7764"}
response = requests.request("POST", url, data=payload, headers=headers)
print(response.text)
````
