# -*- coding: utf-8 -*-#
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, DeleteView, CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from client_account.models import ClientAccount
from .mixins import ManagerAccessMixin
from client_account.forms import ClientAccountForm


class ClientAccountListView(LoginRequiredMixin, ManagerAccessMixin, ListView):
    login_url = reverse_lazy("users:login")
    template_name = "manager/client_account/list.html"
    model = ClientAccount

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context["title"] = "All clients accounts"
        return context


class ClientAccountCreateView(
    LoginRequiredMixin, SuccessMessageMixin, ManagerAccessMixin, CreateView
):
    login_url = reverse_lazy("users:login")
    template_name = "manager/client_account/create.html"
    form_class = ClientAccountForm

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context["title"] = "Create client account"
        return context


class ClientAccountDetailView(
    LoginRequiredMixin, SuccessMessageMixin, ManagerAccessMixin, DetailView
):
    login_url = reverse_lazy("users:login")
    template_name = "manager/client_account/details.html"
    model = ClientAccount

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context["title"] = "Create client account"
        return context
