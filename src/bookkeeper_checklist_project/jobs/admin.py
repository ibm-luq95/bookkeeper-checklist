from django.contrib import admin
from django.template.defaultfilters import truncatechars

from core.admin import BaseAdminModelMixin, JoditEditorAdminMixin
from core.constants.general import DEFAULT_SHORT_TRUNCATED_STRING
from .models import Job, JobTemplate, JobCategory


@admin.register(Job)
class JobAdmin(BaseAdminModelMixin, JoditEditorAdminMixin):
    # list_filter = ("bookkeeper", "job_type", "status", "client")
    list_filter = ("job_type", "status", "client", "is_created_from_template")
    # form = JobForm


@admin.register(JobTemplate)
class JobTemplateAdmin(BaseAdminModelMixin, JoditEditorAdminMixin):
    # list_filter = ("title", "status",)
    list_display = ("get_title", "status", "get_categories")

    def get_categories(self, obj):
        return "\n, ".join([category.name for category in obj.categories.all()])

    def get_title(self, obj):
        return truncatechars(obj.title, DEFAULT_SHORT_TRUNCATED_STRING)


@admin.register(JobCategory)
class JobCategoryTemplateAdmin(BaseAdminModelMixin):
    pass
