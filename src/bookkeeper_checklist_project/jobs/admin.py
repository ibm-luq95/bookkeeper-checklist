from core.admin import BaseAdminModelMixin
from django.contrib import admin

from .models import Job


@admin.register(Job)
class JobAdmin(BaseAdminModelMixin):
    # list_filter = ("bookkeeper", "job_type", "status", "client")
    list_filter = ("job_type", "status", "client")
