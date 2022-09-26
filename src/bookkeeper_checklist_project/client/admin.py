from django.contrib import admin
from .models import Client, ClientAccount


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    pass


@admin.register(ClientAccount)
class ClientAccountAdmin(admin.ModelAdmin):
    pass
