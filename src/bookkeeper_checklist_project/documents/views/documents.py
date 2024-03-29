# -*- coding: utf-8 -*-#
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from core.constants import LIST_VIEW_PAGINATE_BY
from core.utils import get_trans_txt
from core.views.mixins import BaseListViewMixin, BaseLoginRequiredMixin, ListViewMixin
from documents.filters import DocumentsFilter
from documents.forms import DocumentForm
from documents.models import Documents
from manager.views.mixins import ManagerAccessMixin, ManagerAssistantAccessMixin


class ListDocumentView(
    BaseLoginRequiredMixin,
    ManagerAssistantAccessMixin,
    PermissionRequiredMixin,
    BaseListViewMixin,
    ListViewMixin,
    ListView,
):
    permission_required = "documents.can_view_list"
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


class CreateDocumentView(
    BaseLoginRequiredMixin,
    ManagerAssistantAccessMixin,
    PermissionRequiredMixin,
    SuccessMessageMixin,
    BaseListViewMixin,
    CreateView,
):
    permission_required = "documents.add_documents"
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
        url_pattern = f"documents:list"
        url = reverse_lazy(url_pattern)
        return url

    def get_form_kwargs(self):
        kwargs = super(CreateDocumentView, self).get_form_kwargs()
        kwargs.update({"created_by": self.request.user})
        return kwargs


class DetailsDocumentView(
    BaseLoginRequiredMixin,
    ManagerAssistantAccessMixin,
    PermissionRequiredMixin,
    BaseListViewMixin,
    DetailView,
):
    template_name = "documents/show.html"
    model = Documents
    permission_required = "documents.change_documents"


class UpdateDocumentView(
    BaseLoginRequiredMixin,
    PermissionRequiredMixin,
    ManagerAssistantAccessMixin,
    SuccessMessageMixin,
    BaseListViewMixin,
    UpdateView,
):
    permission_required = "documents.change_documents"
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
        url_pattern = f"documents:update"
        url = reverse_lazy(url_pattern, kwargs={"pk": self.get_object().pk})
        return url

    def get_form_kwargs(self):
        """Return the keyword arguments for instantiating the form."""
        kwargs = super().get_form_kwargs()
        sections = ["job", "client", "task"]
        object = self.get_object()
        for sec in sections:
            if sec == object.document_section:
                sections.remove(sec)
        kwargs.update({"is_update": True, "removed_fields": sections})
        return kwargs


class DeleteDocumentView(
    BaseLoginRequiredMixin,
    PermissionRequiredMixin,
    ManagerAssistantAccessMixin,
    SuccessMessageMixin,
    BaseListViewMixin,
    DeleteView,
):
    permission_required = "documents.delete_documents"
    model = Documents
    template_name = "documents/delete.html"
    success_message: str = "Document deleted successfully!"

    def get_success_url(self):
        user_type = self.request.user.user_type
        url_pattern = f"documents:list"
        url = reverse_lazy(url_pattern)
        return url
