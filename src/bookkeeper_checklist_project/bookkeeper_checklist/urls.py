from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from core.utils import get_trans_txt
from core.views import js_settings

static_and_media_path_urls = static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns = [
    # path("admin/", admin.site.urls),  # TODO: add protection package to prevent admin access
    # path("admin/", include("admin_honeypot.urls", namespace="admin_honeypot")),
    path("secret/", admin.site.urls),
    # path(r"^maintenance-mode/", include("maintenance_mode.urls")),
    path("api-auth/", include("rest_framework.urls")),
    path("js-settings/", js_settings, name="js_settings"),
    path("", include("users.urls"), name="users-urls"),
    path("bookkeeper/", include("bookkeeper.urls"), name="bookkeeper-urls"),
    path("assistant/", include("assistant.urls"), name="assistant-urls"),
    path("manager/", include("manager.urls"), name="manager-urls"),
    path("documents/", include("documents.urls"), name="documents-urls"),
    path("notes/", include("notes.urls"), name="notes-urls"),
    path(
        "special_assignment/",
        include("special_assignment.urls"),
        name="special_assignment-urls",
    ),
    path("task/", include("task.urls"), name="task-urls"),
    path("jobs/", include("jobs.urls"), name="jobs-urls"),
    path(
        "important_contact/",
        include("important_contact.urls"),
        name="important_contact-urls",
    ),
    path(
        "company-services/", include("company_services.urls"), name="company-services-urls"
    ),
    path("site-settings/", include("site_settings.urls"), name="site-settings-url"),
]

# set admin configs
admin.site.index_title = get_trans_txt("Bookkeeper Checklist")
admin.site.site_header = get_trans_txt("Bookkeeper Checklist")
admin.site.site_title = get_trans_txt("Bookkeeper Administrator")
# print(settings.LOGGING)
# if settings.DEBUG:
#     urlpatterns += static_and_media_path_urls
#     urlpatterns.append(path("__debug__/", include("debug_toolbar.urls")))
