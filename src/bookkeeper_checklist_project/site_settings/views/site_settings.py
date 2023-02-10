# -*- coding: utf-8 -*-#
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from maintenance_mode.core import set_maintenance_mode

from core.cache import CacheViewMixin
from manager.views.mixins import ManagerAccessMixin
from site_settings.forms import SiteSettingsForm
from site_settings.models import SiteSettings


class SiteSettingsCreateView(
    LoginRequiredMixin, ManagerAccessMixin, SuccessMessageMixin, CacheViewMixin, UpdateView
):
    template_name = "site_settings/site_settings.html"
    login_url = reverse_lazy("users:auth:login")
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

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save()
        if self.object.is_closed is True:
            set_maintenance_mode(True)
        else:
            set_maintenance_mode(False)
        return super().form_valid(form)
