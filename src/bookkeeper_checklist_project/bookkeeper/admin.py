from django.contrib import admin
from .models import Bookkeeper

# Register your models here.
@admin.register(Bookkeeper)
class BookkeeperAdmin(admin.ModelAdmin):
    pass
