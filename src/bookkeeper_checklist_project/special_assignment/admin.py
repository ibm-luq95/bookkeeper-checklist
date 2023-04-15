# from django_summernote.admin import SummernoteModelAdmin

from core.admin import BaseAdminModelMixin, SummernoteAdminMixin
from django.contrib import admin

from .models import SpecialAssignment, Discussion


class DiscussionInline(admin.TabularInline):
    model = Discussion
    fields = ["special_assignment", "body"]
    extra = 0


@admin.register(SpecialAssignment)
class SpecialAssignmentAdmin(BaseAdminModelMixin, SummernoteAdminMixin):
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
class DiscussionAdmin(BaseAdminModelMixin, SummernoteAdminMixin):
    pass
