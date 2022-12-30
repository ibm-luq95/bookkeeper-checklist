# -*- coding: utf-8 -*-#
from django.urls import reverse_lazy

from core.utils import debugging_print
from core.constants.site_settings import WEB_APP_SETTINGS_KEY
from django.contrib.auth import logout
from core.cache import CacheHandler
from django.contrib import messages
from django.shortcuts import redirect


class BookkeeperMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)
        # Code to be executed for each request/response after
        # the view is called.

        return response

    def process_view(self, request, view_func, view_args, view_kwargs):

        if request.user.is_authenticated:

            # check if the user type is bookkeeper or assistants
            if (
                request.user.user_type == "bookkeeper"
                or request.user.user_type == "assistants"
            ):
                site_settings = CacheHandler.get_item(WEB_APP_SETTINGS_KEY)
                if (
                    site_settings.can_bookkeepers_login is False
                    or site_settings.can_assistants_login is False
                ):
                    messages.error(
                        request,
                        "You not allowed to login, please contact the administrator",
                    )
                    logout(request)
                    return redirect(reverse_lazy("users:login"))
