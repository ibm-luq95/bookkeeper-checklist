# -*- coding: utf-8 -*-#
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.db.models import Q
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from client_account.forms import ClientAccountForm
from client_account.models import ClientAccount
from core.utils import get_trans_txt

from .mixins import ManagerAccessMixin


class ClientAccountListView(LoginRequiredMixin, ManagerAccessMixin, ListView):
    login_url = reverse_lazy("users:login")
    template_name = "manager/client_account/list.html"
    model = ClientAccount
    queryset = (
        ClientAccount.objects.select_related()
        .filter(~Q(status__in=["archive"]))
        .order_by("-created_at")
    )

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context["title"] = get_trans_txt("All clients accounts")
        return context


class ClientAccountCreateView(
    LoginRequiredMixin, SuccessMessageMixin, ManagerAccessMixin, CreateView
):
    login_url = reverse_lazy("users:login")
    template_name = "manager/client_account/create.html"
    form_class = ClientAccountForm
    model = ClientAccount
    success_message = get_trans_txt("Client account created successfully!")
    success_url = reverse_lazy("manager:client_account:list")

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context["title"] = get_trans_txt("Create client account")
        return context

    def get_form_kwargs(self):
        kwargs = super(ClientAccountCreateView, self).get_form_kwargs()
        kwargs.update({"created_by": self.request.user})
        return kwargs

    # def get_success_url(self):
    #     url = reverse_lazy(
    #         "manager:client_account:update", kwargs={"pk": self.get_object().pk}
    #     )
    #     return url


class ClientAccountUpdateView(
    LoginRequiredMixin, SuccessMessageMixin, ManagerAccessMixin, UpdateView
):
    login_url = reverse_lazy("users:login")
    template_name = "manager/client_account/update.html"
    form_class = ClientAccountForm
    success_message = get_trans_txt("Client account updated successfully!")
    model = ClientAccount

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context["title"] = get_trans_txt("Update client account")
        return context

    def get_form_kwargs(self):
        kwargs = super(ClientAccountUpdateView, self).get_form_kwargs()
        kwargs.update({"is_update": True, "updated_object": self.get_object()})
        return kwargs

    def get_success_url(self):
        url = reverse_lazy(
            "manager:client_account:update", kwargs={"pk": self.get_object().pk}
        )
        return url


class ClientAccountDetailView(
    LoginRequiredMixin, SuccessMessageMixin, ManagerAccessMixin, DetailView
):
    login_url = reverse_lazy("users:login")
    template_name = "manager/client_account/details.html"
    model = ClientAccount

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context["title"] = get_trans_txt("Client account details")
        return context


class ClientAccountDeleteView(
    LoginRequiredMixin, ManagerAccessMixin, SuccessMessageMixin, DeleteView
):
    login_url = reverse_lazy("users:login")
    model = ClientAccount
    template_name = "manager/client_account/delete.html"
    success_message: str = get_trans_txt("Client account deleted successfully!")
    success_url = reverse_lazy("manager:client_account:list")
