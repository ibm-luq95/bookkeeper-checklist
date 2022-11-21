from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Permission

from core.admin import BaseAdminModelMixin
from .models import CustomUser


@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    pass


@admin.register(CustomUser)
class CustomUserAdmin(BaseAdminModelMixin):
    list_filter = ("user_type", "created_at", "updated_at", "is_active")
    # list_display = ("email",)
