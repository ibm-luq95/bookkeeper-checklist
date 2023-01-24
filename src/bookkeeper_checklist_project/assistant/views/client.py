# -*- coding: utf-8 -*-#
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from client.filters import ClientFilter
from client.forms import ClientForm
from client.models import Client
from core.utils import get_trans_txt
from .mixins import AssistantAccessMixin


class ClientListView(LoginRequiredMixin, AssistantAccessMixin, ListView):
    template_name = "assistant/client/list.html"
    login_url = reverse_lazy("users:login")
    model = Client

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("filter_form", self.filterset.form)
        context.setdefault("title", get_trans_txt("Client"))
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ClientFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs


class ClientDetailsView(LoginRequiredMixin, AssistantAccessMixin, DetailView):
    template_name = "assistant/client/details.html"
    login_url = reverse_lazy("users:login")
    model = Client

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", get_trans_txt("Client"))
        return context


class ClientCreateView(
    LoginRequiredMixin, AssistantAccessMixin, SuccessMessageMixin, CreateView
):
    template_name = "assistant/client/create.html"
    login_url = reverse_lazy("users:login")
    model = Client
    success_message = "Client created successfully"
    success_url = reverse_lazy("assistant:client:list")
    form_class = ClientForm

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", get_trans_txt("Create new client"))
        return context

    def get_form_kwargs(self):
        kwargs = super(ClientCreateView, self).get_form_kwargs()
        kwargs.update({"created_by": self.request.user})
        return kwargs


class ClientUpdateView(
    LoginRequiredMixin, AssistantAccessMixin, SuccessMessageMixin, UpdateView
):
    template_name = "assistant/client/update.html"
    login_url = reverse_lazy("users:login")
    model = Client
    form_class = ClientForm

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", get_trans_txt("Update client"))
        return context
