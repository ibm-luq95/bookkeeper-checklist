from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from bookkeeper.models import Bookkeeper
from core.utils import get_trans_txt

from .mixins import AssistantAccessMixin


class BookkeepersListView(LoginRequiredMixin, AssistantAccessMixin, ListView):
    template_name = "assistant/bookkeepers/list.html"
    login_url = reverse_lazy("users:auth:login")
    model = Bookkeeper

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", get_trans_txt("Bookkeepers"))
        return context


class BookkeepersDetailsView(LoginRequiredMixin, AssistantAccessMixin, DetailView):
    template_name = "assistant/bookkeepers/details.html"
    login_url = reverse_lazy("users:auth:login")
    model = Bookkeeper

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        bookkeeper = self.get_object()
        context.setdefault("title", bookkeeper.user.fullname)
        return context
