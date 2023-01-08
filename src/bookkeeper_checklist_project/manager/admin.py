from core.admin import BaseAdminModelMixin
from manager.models import Manager
from django.contrib import admin

# Register your models here.


@admin.register(Manager)
class ManagerAdmin(BaseAdminModelMixin):
    pass
