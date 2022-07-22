from django.contrib import admin
from .models import CompanyService


@admin.register(CompanyService)
class CompanyServiceAdmin(admin.ModelAdmin):
    pass
