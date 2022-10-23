from core.admin import BaseAdminModelMixin
from django.contrib import admin

from .models import Job


@admin.register(Job)
class JobAdmin(BaseAdminModelMixin):
    pass
