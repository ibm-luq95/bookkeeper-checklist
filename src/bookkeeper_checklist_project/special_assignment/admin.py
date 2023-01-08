from core.admin import BaseAdminModelMixin
from django.contrib import admin

from .models import SpecialAssignment, Discussion


class DiscussionInline(admin.TabularInline):
    model = Discussion
    fields = ["special_assignment", "title", "body"]
    extra = 0

@admin.register(SpecialAssignment)
class SpecialAssignmentAdmin(BaseAdminModelMixin):
    list_filter = (
        "is_seen",
        "start_date",
        "due_date",
        "status",
        "created_at",
        "updated_at",
    )
    inlines = [DiscussionInline]


@admin.register(Discussion)
class DiscussionAdmin(BaseAdminModelMixin):
    pass
