from django.contrib import admin
from .models import BankAccountItem, BankProfile, BankUserAccount

# Register your models here.
@admin.register(BankProfile)
class BankProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(BankUserAccount)
class BankUserAccountAdmin(admin.ModelAdmin):
    pass


@admin.register(BankAccountItem)
class BankAccountItemAdmin(admin.ModelAdmin):
    pass
