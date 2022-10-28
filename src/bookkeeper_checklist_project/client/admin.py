from bookkeeper.models import Bookkeeper
from core.admin import BaseAdminModelMixin
from django.contrib import admin

from .models import Client, ClientAccount, ImportantContact


class BookkeeperInline(admin.TabularInline):
    model = Bookkeeper.clients.through
    extra = 2


@admin.register(Client)
class ClientAdmin(BaseAdminModelMixin):
    inlines = (BookkeeperInline,)


@admin.register(ClientAccount)
class ClientAccountAdmin(BaseAdminModelMixin):
    pass


@admin.register(ImportantContact)
class ImportantContactAdmin(BaseAdminModelMixin):
    pass
