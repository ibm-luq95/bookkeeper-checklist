# -*- coding: utf-8 -*-#
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from core.cache import CacheViewMixin
from core.utils import get_trans_txt
from core.views.mixins import BaseLoginRequiredMixin
from manager.views.mixins import ManagerAccessMixin
from site_settings.forms import ApplicationConfigurationsForm
from site_settings.models import ApplicationConfigurations


class ApplicationConfigurationsFormView(
    BaseLoginRequiredMixin,
    ManagerAccessMixin,
    SuccessMessageMixin,
    CacheViewMixin,
    UpdateView,
):
    template_name = "site_settings/application_configuration.html"
    form_class = ApplicationConfigurationsForm
    success_url = reverse_lazy("site_settings:app-configs-settings")
    success_message = get_trans_txt("Application configurations updated successfully!")
    model = ApplicationConfigurations

    def get_object(self, queryset=None):
        obj = self.model.objects.filter(slug="app-configs").first()
        if not obj:
            messages.warning(self.request, "No app configs!")
        return obj

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", get_trans_txt("Application configurations"))
        return context
