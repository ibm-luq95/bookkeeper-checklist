from core.admin import BaseAdminModelMixin
from django.contrib import admin

from .models import SpecialAssignment


@admin.register(SpecialAssignment)
class SpecialAssignmentAdmin(BaseAdminModelMixin):
    list_filter = ("is_seen", "start_date", "due_date", "status")
