# -*- coding: utf-8 -*-#
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
    RedirectView,
)

from client.forms import ClientCategoryForm
from core.constants import LIST_VIEW_PAGINATE_BY
from core.utils import get_trans_txt
from core.views.mixins import BaseListViewMixin, BaseLoginRequiredMixin
from manager.views.mixins import ManagerAssistantAccessMixin
from client.models import ClientCategory


class ClientCategoryListView(
    BaseLoginRequiredMixin,
    PermissionRequiredMixin,
    ManagerAssistantAccessMixin,
    BaseListViewMixin,
    ListView,
):
    permission_required = "clientcategory.can_view_list"
    model = ClientCategory
    template_name = "client/category/list.html"
    paginate_by = LIST_VIEW_PAGINATE_BY

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", get_trans_txt("Clients categories"))
        return context


class ClientCategoryCreateView(
    BaseLoginRequiredMixin,
    PermissionRequiredMixin,
    ManagerAssistantAccessMixin,
    SuccessMessageMixin,
    CreateView,
):
    model = ClientCategory
    form_class = ClientCategoryForm
    template_name = "client/category/create.html"
    permission_required = "clientcategory.add_clientcategory"
    success_message = get_trans_txt("Category created successfully")
    success_url = reverse_lazy("client:category:list")

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", get_trans_txt("Create category"))
        return context


class ClientCategoryUpdateView(
    BaseLoginRequiredMixin,
    PermissionRequiredMixin,
    ManagerAssistantAccessMixin,
    SuccessMessageMixin,
    UpdateView,
):
    model = ClientCategory
    form_class = ClientCategoryForm
    template_name = "client/category/update.html"
    permission_required = "clientcategory.change_clientcategory"
    success_message = get_trans_txt("Category updated successfully")
    success_url = reverse_lazy("client:category:list")

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", get_trans_txt("Update category"))
        return context


class ClientCategoryDeleteView(
    BaseLoginRequiredMixin,
    PermissionRequiredMixin,
    ManagerAssistantAccessMixin,
    SuccessMessageMixin,
    DeleteView,
):
    model = ClientCategory
    template_name = "client/category/delete.html"
    permission_required = "clientcategory.delete_clientcategory"
    success_message = get_trans_txt("Category deleted successfully")
    success_url = reverse_lazy("client:category:list")

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", get_trans_txt("Delete category"))
        return context
