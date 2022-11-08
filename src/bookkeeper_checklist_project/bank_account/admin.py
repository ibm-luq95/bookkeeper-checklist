from core.admin import BaseAdminModelMixin
from django.contrib import admin

from .models import BankAccountItem, BankProfile, BankUserAccount


# Register your models here.
@admin.register(BankProfile)
class BankProfileAdmin(BaseAdminModelMixin):
    pass


@admin.register(BankUserAccount)
class BankUserAccountAdmin(BaseAdminModelMixin):
    pass


@admin.register(BankAccountItem)
class BankAccountItemAdmin(BaseAdminModelMixin):
    pass
