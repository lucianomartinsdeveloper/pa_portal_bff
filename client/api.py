from typing import List

from django.shortcuts import get_object_or_404
from ninja import Router, Schema

from ninja.orm import create_schema

from .models import Client

router = Router()

ClientSchema = create_schema(Client)

class ClientSchemaIn(Schema):
    name: str

@router.get('/clients', response=List[ClientSchema])
def list_clients(request):
    return Client.objects.all()

@router.get('/clients/{id}', response=ClientSchema)
def get_client(request, id: int):
    return get_object_or_404(Client, id=id)

@router.post('/clients', response={201: ClientSchema})
def create_client(request, payload: ClientSchemaIn):
    return Client.objects.create(**payload.dict())

@router.put('/client/{id}', response=ClientSchema)
def update_client(request, id: int, payload: ClientSchemaIn):
    client = get_object_or_404(Client, id=id)

    for attr, value in payload.dict().items():
        setattr(client, attr, value)
    client.save()
    return client

@router.delete('/clients/{id}', response={204: None})
def delete_client(request, id: int):
    client = get_object_or_404(Client, id=id)
    client.delete()
    return 204, None
