# -*- coding: utf-8 -*-#
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, DeleteView, CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from client.models import Client
from .mixins import ManagerAccessMixin
from client.forms import ClientForm


class ClientListView(LoginRequiredMixin, ManagerAccessMixin, ListView):
    login_url = reverse_lazy("users:login")
    template_name = "manager/client/list.html"
    model = Client

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context["title"] = "All clients"
        return context


class ClientCreateView(
    LoginRequiredMixin, SuccessMessageMixin, ManagerAccessMixin, CreateView
):
    login_url = reverse_lazy("users:login")
    template_name = "manager/client/create.html"
    form_class = ClientForm

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context["title"] = "Create client"
        return context
