# -*- encoding: utf-8 -*-
from django_summernote.admin import SummernoteModelAdmin


class SummernoteAdminMixin(SummernoteModelAdmin):
# class SummernoteAdminMixin:
    summernote_fields = "__all__"
