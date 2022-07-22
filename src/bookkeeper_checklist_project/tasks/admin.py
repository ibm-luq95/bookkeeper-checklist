from django.contrib import admin
from .models import Task, TaskItem


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass


@admin.register(TaskItem)
class TaskItemAdmin(admin.ModelAdmin):
    pass
