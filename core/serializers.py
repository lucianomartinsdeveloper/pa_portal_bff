import string
from datetime import datetime

from djoser.serializers import (
    UserCreateSerializer as BaseUserRegistrationSerializer,
)
from rest_framework import serializers

from core.models import User


class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    username = serializers.CharField(required=True)
    birth_date = serializers.DateField(required=True)
    type_of_audience = serializers.CharField(required=True)

    class Meta(BaseUserRegistrationSerializer.Meta):
        model = User
        fields = (
            "email",
            "username",
            "birth_date",
            "type_of_audience",
            "password",
        )

    def validate_username(self, value):
        has_char_phroibithed = any(char in string.punctuation for char in value)
        if has_char_phroibithed:
            raise serializers.ValidationError("Só letras para o campo NOME.")
        if len(value) < 3:
            raise serializers.ValidationError("Nome tem quer mais de 3 letras.")
        return value

    def validate_birth_date(self, value):
        data_atual = datetime.now()
        data_nascimento = value
        idade = data_atual.year - value.year
        if data_nascimento.month > data_atual.month or (
            data_nascimento.month == data_atual.month
            and data_nascimento.day > data_atual.day
        ):
            idade -= 1
        if idade < 18:
            raise serializers.ValidationError("Tem que ser maior de idade.")
        return value
