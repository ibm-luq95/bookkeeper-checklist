# from django_summernote.admin import SummernoteModelAdmin

from core.admin import BaseAdminModelMixin, JoditEditorAdminMixin
from django.contrib import admin

from .models import Task, TaskTemplate, TaskItem


@admin.register(Task)
class TaskAdmin(BaseAdminModelMixin, JoditEditorAdminMixin):
    # pass
    # list_filter = ("is_completed", "start_date", "due_date", "task_type")
    list_filter = ("is_completed",)
    summernote_fields = ("additional_notes",)


@admin.register(TaskTemplate)
class TaskTemplateAdmin(BaseAdminModelMixin, JoditEditorAdminMixin):
    pass


@admin.register(TaskItem)
class TaskItemAdmin(BaseAdminModelMixin):
    pass
