from django.contrib import admin
from core.admin import BaseAdminModelMixin
from .models import Client, ClientAccount, ImportantContact


@admin.register(Client)
class ClientAdmin(BaseAdminModelMixin):
    pass


@admin.register(ClientAccount)
class ClientAccountAdmin(BaseAdminModelMixin):
    pass


@admin.register(ImportantContact)
class ImportantContactAdmin(BaseAdminModelMixin):
    pass
