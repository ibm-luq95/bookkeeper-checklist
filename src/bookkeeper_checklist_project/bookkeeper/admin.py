from core.admin import BaseAdminModelMixin
from django.contrib import admin

from .models import Bookkeeper


# Register your models here.
@admin.register(Bookkeeper)
class BookkeeperAdmin(BaseAdminModelMixin):
    list_filter = ("is_active",)
