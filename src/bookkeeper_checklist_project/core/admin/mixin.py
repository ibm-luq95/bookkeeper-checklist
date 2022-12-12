from django.contrib import admin


class BaseAdminModelMixin(admin.ModelAdmin):
    list_filter = ("created_at", "updated_at")
    exclude = ("metadata", "is_deleted",)
    # list_display = ["created_at", "is_deleted"]
