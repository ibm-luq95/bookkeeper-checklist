from django.contrib import admin

from company_services.models import CompanyService
from core.admin import BaseAdminModelMixin


@admin.register(CompanyService)
class CompanyServiceAdmin(BaseAdminModelMixin):
    pass
