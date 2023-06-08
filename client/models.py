from django.db import models


# class Local(models.Model):
#     _DATABASE = 'default'
#
# class Remote(models.Model):
#     _DATABASE = 'remote'

class Client(models.Model):
    name = models.CharField(
        'Nome',
        max_length=120,
        null=False, blank=False
    )
    email = models.CharField(
        'Email',
        max_length=100,
        null=True,
    )
    birth_date = models.DateField(
        "Data de Nascimento",
        null=True
    )
    registered = models.BooleanField(
        'Inscrito',
        default=False
    )
    subscriber = models.BooleanField(
        'Assinante',
        default=False
    )
    is_deleted = models.BooleanField(
        default=False
    )
    deleted_at = models.DateTimeField(
        "Data Delecao",
        null=True,
    )
    address = models.ForeignKey(
        'Address',
        on_delete=models.CASCADE,
        related_name='addressies',
        blank=True, null=True,
    )
    telephone = models.ForeignKey(
        'Telephone',
        on_delete=models.CASCADE,
        related_name='telephones',
        blank=True, null=True,
    )
    is_active = models.BooleanField(
        'Ativo',
        default=True
    )
    created = models.DateTimeField(
        auto_now_add=True
    )
    updated = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"


class Telephone(models.Model):
    TYPE_PHONE = [
        ("cel", "Celular"),
        ("fix", "Fixo"),
    ]

    number = models.CharField(
        'Número',
        max_length=20
    )
    type = models.CharField(
        'Número',
        choices=TYPE_PHONE,
        max_length=3
    )

    def __str__(self):
        return f'{self.number}'

    class Meta:
        verbose_name = 'Telefone'
        verbose_name_plural = 'Telefones'


class Address(models.Model):
    public_place = models.CharField(
        'Logradouro',
        max_length=100
    )
    neighborhood = models.CharField(
        "Bairro",
        max_length=255,
        blank=True
    )
    city = models.CharField(
        "Cidade",
        max_length=50,
        blank=True
    )
    zip_code = models.IntegerField(
        'CEP'
    )
    number = models.IntegerField(
        'Número'
    )
    complement = models.CharField(
        'Complemento',
        max_length=10,
        null=True, blank=True
    )

    def __str__(self):
        return f'{self.public_place}, {self.number} - {self.complement}'

    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'
