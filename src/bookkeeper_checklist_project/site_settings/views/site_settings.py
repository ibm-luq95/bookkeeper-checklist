# -*- coding: utf-8 -*-#
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from manager.views.mixins import ManagerAccessMixin
from site_settings.forms import SiteSettingsForm
from site_settings.models import SiteSettings


class SiteSettingsCreateView(
    LoginRequiredMixin, ManagerAccessMixin, SuccessMessageMixin, UpdateView
):
    template_name = "site_settings/site_settings.html"
    login_url = reverse_lazy("users:login")
    form_class = SiteSettingsForm
    success_url = reverse_lazy("site_settings:web-app-settings")
    success_message = "Web application settings updated successfully!"
    model = SiteSettings

    def get_object(self, queryset=None):
        obj = self.model.objects.select_related().filter(slug="web-app").first()
        if not obj:
            messages.warning(self.request, "No web app settings!")

        return obj

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context["title"] = "Web app settings"
        return context
