from django.contrib import admin
from .models import Assistant


@admin.register(Assistant)
class AssistantAdmin(admin.ModelAdmin):
    pass
