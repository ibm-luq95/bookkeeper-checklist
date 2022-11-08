from core.admin import BaseAdminModelMixin
from django.contrib import admin

from .models import Task


@admin.register(Task)
class TaskAdmin(BaseAdminModelMixin):
    list_filter = ("is_completed", "start_date", "due_date")
