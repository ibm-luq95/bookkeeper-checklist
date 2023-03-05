from django.contrib import admin

from bookkeeper.models import Bookkeeper
from core.admin import BaseAdminModelMixin
from core.constants import ADMIN_FILTER_LIST
from .models import Client, ClientCategory


# class BookkeeperInline(admin.TabularInline):
#     model = Bookkeeper.clients.through
#     extra = 2


@admin.register(Client)
class ClientAdmin(BaseAdminModelMixin):
    # inlines = (BookkeeperInline,)
    list_display = ["name", "email", "industry", "created_at", "is_active", "is_deleted"]
    list_filter = ADMIN_FILTER_LIST + ["is_deleted", "is_active"]


@admin.register(ClientCategory)
class ClientCategoryAdmin(BaseAdminModelMixin):
    pass
