from django.contrib import admin


class BaseAdminModelMixin(admin.ModelAdmin):
    exclude = ("metadata", "is_deleted",)
