from rest_framework import status
from rest_framework.test import APIClient


client = APIClient()


def test_create_user(db):
    data = {
        "username": "Salomão Garu da Silva",
        "email": "salomao@gmail.com",
        "password": "mudar123",
        "birth_date": "2003-06-20",
        "type_of_audience": "PRO",
    }
    response = client.post("/api/v1/users/", data=data)
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json()["username"] == data["username"]
    assert response.json()["birth_date"] == data["birth_date"]


def test_email_invalid(db):
    data = {
        "birth_date": "2005-05-05",
        "email": "p.com",
        "password": "luxu1650",
        "type_of_audience": "PRO",
        "username": "Pedro",
    }
    response = client.post("/api/v1/users/", data=data)
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json() == {"email": ["Insira um endereço de email válido."]}


def test_create_user_less_than_3_letters(db):
    data = {
        "birth_date": "2005-05-05",
        "email": "p1@p.com",
        "password": "luxu1650",
        "type_of_audience": "PRO",
        "username": "Pe",
    }
    response = client.post("/api/v1/users/", data=data)
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json() == {"username": ["Nome tem quer mais de 3 letras."]}


def test_must_be_of_legal_age(db):
    data = {
        "birth_date": "2005-06-22",
        "email": "p1@p.com",
        "password": "luxu1650",
        "type_of_audience": "PRO",
        "username": "Pedro",
    }
    response = client.post("/api/v1/users/", data=data)
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json() == {"birth_date": ["Tem que ser maior de idade."]}


def test_field_type_od_audience_empty(db):
    data = {
        "birth_date": "2005-06-20",
        "email": "p1@p.com",
        "password": "luxu1650",
        "type_of_audience": "",
        "username": "Pedro",
    }
    response = client.post("/api/v1/users/", data=data)
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json() == {
        "type_of_audience": ["Este campo não pode ser em branco."]
    }
