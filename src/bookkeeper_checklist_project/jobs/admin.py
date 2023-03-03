from core.admin import BaseAdminModelMixin
from django.contrib import admin

from .models import Job, JobTemplate, JobCategory


@admin.register(Job)
class JobAdmin(BaseAdminModelMixin):
    # list_filter = ("bookkeeper", "job_type", "status", "client")
    list_filter = ("job_type", "status", "client")


@admin.register(JobTemplate)
class JobTemplateAdmin(BaseAdminModelMixin):
    pass


@admin.register(JobCategory)
class JobCategoryTemplateAdmin(BaseAdminModelMixin):
    pass
