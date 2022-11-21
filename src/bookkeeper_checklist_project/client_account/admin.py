from core.admin import BaseAdminModelMixin
from django.contrib import admin

from client_account.models import ClientAccount
from core.constants import ADMIN_FILTER_LIST


@admin.register(ClientAccount)
class ClientAccountAdmin(BaseAdminModelMixin):
    list_display = [
        "client",
        "account_name",
        "account_email",
        "created_at",
        "updated_at",
        "is_deleted",
    ]
