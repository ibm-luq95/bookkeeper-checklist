# -*- coding: utf-8 -*-#

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.db.models import Q
from django.views.generic import DeleteView, DetailView, ListView, CreateView, UpdateView

from core.constants import LIST_VIEW_PAGINATE_BY
from core.views.mixins import BaseListViewMixin
from manager.models import Manager
from manager.forms import ManagerForm, ManagerUpdateForm
from core.utils import get_trans_txt
from .mixins import ManagerAccessMixin


class ManagerListView(LoginRequiredMixin, ManagerAccessMixin, BaseListViewMixin, ListView):
    login_url = reverse_lazy("users:auth:login")
    template_name: str = "manager/manager/list.html"
    model = Manager
    queryset = (
        Manager.objects.select_related()
        .filter(~Q(status="archive"))
        .order_by("-created_at")
    )
    list_type = "list"

    paginate_by: int = LIST_VIEW_PAGINATE_BY

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", get_trans_txt("All managers"))
        context.setdefault("page_header", "Managers ".capitalize())
        context.setdefault("list_type", self.list_type)
        return context


class ManagerCreateView(
    LoginRequiredMixin, ManagerAccessMixin, SuccessMessageMixin, CreateView
):
    login_url = reverse_lazy("users:auth:login")
    template_name: str = "manager/manager/create.html"
    model = Manager
    success_message = get_trans_txt("Manager created successfully")
    form_class = ManagerForm
    success_url = reverse_lazy("manager:manager:list")

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context["title"] = get_trans_txt("Create manager")
        return context


class ManagerDeleteView(
    LoginRequiredMixin, ManagerAccessMixin, SuccessMessageMixin, DeleteView
):
    login_url = reverse_lazy("users:auth:login")
    model = Manager
    template_name = "manager/manager/delete.html"
    success_message: str = get_trans_txt("Manager deleted successfully!")
    success_url = reverse_lazy("manager:manager:list")


class ManagerArchiveView(
    LoginRequiredMixin, ManagerAccessMixin, BaseListViewMixin, ListView
):
    login_url = reverse_lazy("users:auth:login")
    template_name: str = "manager/manager/archive_list.html"
    model = Manager
    queryset = (
        Manager.objects.select_related().filter(Q(status="archive")).order_by("-created_at")
    )
    list_type = "archive"

    paginate_by: int = LIST_VIEW_PAGINATE_BY

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", get_trans_txt("All archived manager"))
        context.setdefault("page_header", "archived managers".capitalize())
        context.setdefault("list_type", self.list_type)
        return context


class ManagerUpdateView(
    LoginRequiredMixin, ManagerAccessMixin, SuccessMessageMixin, UpdateView
):
    login_url = reverse_lazy("users:auth:login")
    template_name: str = "manager/manager/update.html"
    model = Manager
    success_message = get_trans_txt("Manager updated successfully")
    form_class = ManagerUpdateForm
    success_url = reverse_lazy("manager:manager:list")

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", get_trans_txt("Update manager"))
        return context


class ManagerDetailsView(LoginRequiredMixin, ManagerAccessMixin, DetailView):
    login_url = reverse_lazy("users:auth:login")
    template_name: str = "manager/manager/details.html"
    model = Manager

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("tite", f"Manager - {self.get_object().user.fullname}")
        return context
