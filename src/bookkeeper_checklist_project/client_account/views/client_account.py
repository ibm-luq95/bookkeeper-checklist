# -*- coding: utf-8 -*-#
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from client_account.filters import ClientAccountFilter
from client_account.forms import ClientAccountForm
from client_account.models import ClientAccount
from core.constants import LIST_VIEW_PAGINATE_BY
from core.utils import get_trans_txt
from core.views.mixins import BaseListViewMixin, BaseLoginRequiredMixin
from manager.views.mixins import ManagerAccessMixin


class ClientAccountListView(
    BaseLoginRequiredMixin, ManagerAccessMixin, BaseListViewMixin, ListView
):
    template_name = "client_account/list.html"
    model = ClientAccount
    queryset = (
        ClientAccount.objects.select_related()
        .filter(~Q(status__in=["archive"]))
        .order_by("-created_at")
    )
    paginate_by = LIST_VIEW_PAGINATE_BY

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("filter_form", self.filterset.form)
        context.setdefault("title", get_trans_txt("All clients accounts"))
        context.setdefault("page_header", "clients accounts".title())
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ClientAccountFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs


class ClientAccountCreateView(
    BaseLoginRequiredMixin,
    SuccessMessageMixin,
    ManagerAccessMixin,
    BaseListViewMixin,
    CreateView,
):
    template_name = "client_account/create.html"
    form_class = ClientAccountForm
    model = ClientAccount
    success_message = get_trans_txt("Client account created successfully!")
    success_url = reverse_lazy("accounts:list")

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
    BaseLoginRequiredMixin,
    SuccessMessageMixin,
    ManagerAccessMixin,
    BaseListViewMixin,
    UpdateView,
):
    template_name = "client_account/update.html"
    form_class = ClientAccountForm
    success_message = get_trans_txt("Client account updated successfully!")
    model = ClientAccount

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", get_trans_txt("Update client account"))
        return context

    def get_form_kwargs(self):
        kwargs = super(ClientAccountUpdateView, self).get_form_kwargs()
        kwargs.update({"is_update": True, "updated_object": self.get_object()})
        return kwargs

    def get_success_url(self):
        url = reverse_lazy("accounts:update", kwargs={"pk": self.get_object().pk})
        return url


class ClientAccountDetailsView(
    BaseLoginRequiredMixin,
    SuccessMessageMixin,
    ManagerAccessMixin,
    BaseListViewMixin,
    DetailView,
):
    template_name = "client_account/details.html"
    model = ClientAccount

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context["title"] = get_trans_txt("Client account details")
        return context


class ClientAccountDeleteView(
    BaseLoginRequiredMixin,
    ManagerAccessMixin,
    SuccessMessageMixin,
    BaseListViewMixin,
    DeleteView,
):
    model = ClientAccount
    template_name = "client_account/delete.html"
    success_message: str = get_trans_txt("Client account deleted successfully!")
    success_url = reverse_lazy("accounts:list")
