from core.admin import BaseAdminModelMixin
from django.contrib import admin

from .models import Assistant


@admin.register(Assistant)
class AssistantAdmin(BaseAdminModelMixin):
    pass
