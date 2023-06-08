from django.contrib import admin

from client.models import Client, Telephone, Address


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'birth_date',
        'registered',
        'subscriber',
        'is_active',
    )
    search_fields = ('name',)


@admin.register(Telephone)
class TelephoneAdmin(admin.ModelAdmin):
    list_display = ('number', 'type',)
    search_fields = ('number',)


@admin.register(Address)
class AddresstAdmin(admin.ModelAdmin):
    list_display = ('__str__',)
    search_fields = ('public_place',)
