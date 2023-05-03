# -*- coding: utf-8 -*-#
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, CreateView, UpdateView

from client.models import Client
from core.constants import LIST_VIEW_PAGINATE_BY
from core.utils import get_trans_txt
from core.views.mixins import BaseListViewMixin, BaseLoginRequiredMixin, ListViewMixin
from notes.models import Note
from notes.forms import NoteForm
from notes.filters import NotesFilter
from manager.views.mixins import ManagerAccessMixin, ManagerAssistantAccessMixin


class NoteListView(
    BaseLoginRequiredMixin,
    ManagerAssistantAccessMixin,
    PermissionRequiredMixin,
    BaseListViewMixin,
    ListViewMixin,
    ListView,
):
    template_name = "notes/list.html"
    model = Note
    http_method_names = ["get"]
    paginate_by = LIST_VIEW_PAGINATE_BY
    permission_required = "notes.can_view_list"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", get_trans_txt("All notes"))
        context.setdefault("filter_form", self.filterset.form)
        context.setdefault("page_header", "notes".title())
        # print(self.filterset.form["contact_name"])
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = NotesFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs


class NoteCreateView(
    BaseLoginRequiredMixin,
    PermissionRequiredMixin,
    ManagerAssistantAccessMixin,
    SuccessMessageMixin,
    BaseListViewMixin,
    CreateView,
):
    permission_required = "notes.add_note"
    template_name = "notes/create.html"
    model = Note
    http_method_names = ["get", "post"]
    form_class = NoteForm
    success_message = get_trans_txt("Note created successfully")
    success_url = reverse_lazy("notes:list")

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", "Create note")
        return context

    def get_form_kwargs(self):
        kwargs = super(NoteCreateView, self).get_form_kwargs()
        client_pk = self.request.GET.get("client")
        kwargs.update({"add_jodit_css_class": True})
        kwargs.update({"created_by": self.request.user})
        if client_pk is not None:
            kwargs.update({"client_pk": client_pk})
        return kwargs


class NotesUpdateView(
    BaseLoginRequiredMixin,
    ManagerAssistantAccessMixin,
    PermissionRequiredMixin,
    SuccessMessageMixin,
    BaseListViewMixin,
    UpdateView,
):
    permission_required = "notes.change_note"
    template_name = "notes/update.html"
    model = Note
    http_method_names = ["get", "post"]
    form_class = NoteForm
    success_message = get_trans_txt("Note update successfully")
    success_url = reverse_lazy("notes:list")

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", get_trans_txt("Update note"))

        return context

    def get_form_kwargs(self):
        kwargs = super(NotesUpdateView, self).get_form_kwargs()
        sections = ["job", "client", "task"]
        object = self.get_object()
        kwargs.update({"add_jodit_css_class": True})
        for sec in sections:
            if sec == object.note_section:
                sections.remove(sec)
        kwargs.update({"removed_fields": sections})
        return kwargs


class NoteDeleteView(
    BaseLoginRequiredMixin,
    ManagerAssistantAccessMixin,
    PermissionRequiredMixin,
    SuccessMessageMixin,
    BaseListViewMixin,
    DeleteView,
):
    permission_required = "notes.delete_note"
    template_name = "notes/delete.html"
    model = Note
    http_method_names = ["get", "post"]
    success_message = get_trans_txt("Note deleted successfully")
    success_url = reverse_lazy("notes:list")

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context["title"] = get_trans_txt("Delete note")
        return context
