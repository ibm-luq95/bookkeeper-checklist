# from django_summernote.admin import SummernoteModelAdmin

from core.admin import BaseAdminModelMixin, SummernoteAdminMixin
from django.contrib import admin

from .models import Task, TaskTemplate, TaskItem


@admin.register(Task)
class TaskAdmin(BaseAdminModelMixin, SummernoteAdminMixin):
    # pass
    # list_filter = ("is_completed", "start_date", "due_date", "task_type")
    list_filter = ("is_completed",)
    summernote_fields = ("additional_notes",)


@admin.register(TaskTemplate)
class TaskTemplateAdmin(BaseAdminModelMixin, SummernoteAdminMixin):
    pass


@admin.register(TaskItem)
class TaskItemAdmin(BaseAdminModelMixin):
    pass
