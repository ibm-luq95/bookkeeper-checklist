# -*- coding: utf-8 -*-#
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from core.constants import LIST_VIEW_PAGINATE_BY
from core.utils import get_trans_txt
from core.views.mixins import BaseListViewMixin
from documents.filters import DocumentsFilter
from documents.forms import DocumentForm
from documents.models import Documents
from manager.views.mixins import ManagerAccessMixin


class ManagerListDocumentView(
    LoginRequiredMixin, ManagerAccessMixin, BaseListViewMixin, ListView
):
    login_url = reverse_lazy("users:auth:login")
    template_name = "documents/list.html"
    model = Documents
    paginate_by = LIST_VIEW_PAGINATE_BY
    list_type = "list"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", get_trans_txt("All documents"))
        context.setdefault("list_type", self.list_type)
        context.setdefault("page_header", "all documents".title())
        context.setdefault("filter_form", self.filterset.form)

        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = DocumentsFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs


class ManagerCreateDocumentView(
    LoginRequiredMixin,
    ManagerAccessMixin,
    SuccessMessageMixin,
    BaseListViewMixin,
    CreateView,
):
    login_url = reverse_lazy("users:auth:login")
    template_name = "documents/create.html"
    form_class = DocumentForm
    success_message = get_trans_txt("Document Created Successfully")

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", get_trans_txt("create document".capitalize()))

        return context

    def get_success_url(self):
        user_type = self.request.user.user_type
        url_pattern = f"documents:{user_type}:list"
        url = reverse_lazy(url_pattern)
        return url

    def get_form_kwargs(self):
        kwargs = super(ManagerCreateDocumentView, self).get_form_kwargs()
        kwargs.update({"created_by": self.request.user})
        return kwargs


class ManagerDetailsDocumentView(
    LoginRequiredMixin, ManagerAccessMixin, BaseListViewMixin, DetailView
):
    login_url = reverse_lazy("users:auth:login")
    template_name = "documents/show.html"
    model = Documents


class ManagerUpdateDocumentView(
    LoginRequiredMixin,
    ManagerAccessMixin,
    SuccessMessageMixin,
    BaseListViewMixin,
    UpdateView,
):
    login_url = reverse_lazy("users:auth:login")
    template_name = "documents/update.html"
    form_class = DocumentForm
    success_message = get_trans_txt("Document updated successfully")
    model = Documents

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", "Update document")

        return context

    def get_success_url(self):
        user_type = self.request.user.user_type
        url_pattern = f"documents:{user_type}:update"
        url = reverse_lazy(url_pattern, kwargs={"pk": self.get_object().pk})
        return url

    def get_form_kwargs(self):
        """Return the keyword arguments for instantiating the form."""
        kwargs = super().get_form_kwargs()
        kwargs.update({"is_update": True})
        return kwargs


class ManagerDeleteDocumentView(
    LoginRequiredMixin,
    ManagerAccessMixin,
    SuccessMessageMixin,
    BaseListViewMixin,
    DeleteView,
):
    login_url = reverse_lazy("users:auth:login")
    model = Documents
    template_name = "documents/delete.html"
    success_message: str = "Document deleted successfully!"

    def get_success_url(self):
        user_type = self.request.user.user_type
        url_pattern = f"documents:{user_type}:list"
        url = reverse_lazy(url_pattern)
        return url
