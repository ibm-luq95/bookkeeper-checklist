from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView

from .mixins import AssistantAccessMixin


class DashboardView(LoginRequiredMixin, AssistantAccessMixin, TemplateView):
    template_name = "assistant/dashboard/dashboard.html"
    login_url = reverse_lazy("users:login")

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context["title"] = "Assistant - Dashboard"
        return context
