import string
from datetime import datetime

from djoser.compat import get_user_email, get_user_email_field_name
from djoser.conf import settings
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


class ListUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    # class UserSerializer(serializers.ModelSerializer):
    # class Meta:
    #     model = User
    #     fields = tuple(User.REQUIRED_FIELDS) + (
    #         settings.USER_ID_FIELD,
    #         settings.LOGIN_FIELD,
    #     )
    #     read_only_fields = (settings.LOGIN_FIELD,)

    def update(self, instance, validated_data):
        email_field = get_user_email_field_name(User)
        instance.email_changed = False
        if settings.SEND_ACTIVATION_EMAIL and email_field in validated_data:
            instance_email = get_user_email(instance)
            if instance_email != validated_data[email_field]:
                instance.is_active = False
                instance.email_changed = True
                instance.save(update_fields=["is_active"])
        return super().update(instance, validated_data)


# class CustomTokenSerializer(TokenSerializer):
#     def to_representation(self, instance):
#         data = super().to_representation(instance)
#         # Adicione os campos do usuário que você deseja retornar
#         token = data['auth_token']
#         User.objects.filter()
#         user = self.context['request'].user
#         data['username'] = user.username
#         data['email'] = user.email
#         # Adicione mais campos personalizados conforme necessário
#         return data
