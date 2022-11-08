from core.utils import get_trans_txt
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from core.views import js_settings


static_and_media_path_urls = static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


urlpatterns = [
    path("admin/", admin.site.urls),  # TODO: add protection package to prevent admin access
    path('api-auth/', include('rest_framework.urls')),
    path("js-settings/", js_settings, name="js_settings"),
    path("__debug__/", include("debug_toolbar.urls")),
    path("", include("users.urls"), name="users-urls"),
    path("bookkeeper/", include("bookkeeper.urls"), name="bookkeeper-urls"),
    path("assistant/", include("assistant.urls"), name="assistant-urls"),
    path("manager/", include("manager.urls"), name="manager-urls"),
]

# set admin configs
admin.site.index_title = get_trans_txt("Bookkeeper Checklist")
admin.site.site_header = get_trans_txt("Bookkeeper Checklist")
admin.site.site_title = get_trans_txt("Bookkeeper Administrator")

if settings.DEBUG:
    urlpatterns += static_and_media_path_urls
