from django.contrib import admin

from core.admin import BaseAdminModelMixin
from important_contact.models import ImportantContact


@admin.register(ImportantContact)
class ImportantContactAdmin(BaseAdminModelMixin):
    pass
