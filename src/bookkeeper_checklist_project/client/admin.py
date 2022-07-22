from django.contrib import admin
from .models import Client, ClientAccount, ClientBusinessProfile


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    pass


@admin.register(ClientAccount)
class ClientAccountAdmin(admin.ModelAdmin):
    pass


@admin.register(ClientBusinessProfile)
class ClientBusinessProfileAdmin(admin.ModelAdmin):
    pass
