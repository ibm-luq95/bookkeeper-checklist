from core.admin import BaseAdminModelMixin
from django.contrib import admin

from .models import Task


@admin.register(Task)
class TaskAdmin(BaseAdminModelMixin):
    pass
