from core.admin import BaseAdminModelMixin
from django.contrib import admin

from .models import CompanyService


@admin.register(CompanyService)
class CompanyServiceAdmin(BaseAdminModelMixin):
    pass
