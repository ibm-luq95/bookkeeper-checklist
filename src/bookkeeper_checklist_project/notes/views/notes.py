# -*- coding: utf-8 -*-#
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, CreateView, UpdateView

from client.models import Client
from core.constants import LIST_VIEW_PAGINATE_BY
from core.utils import get_trans_txt
from core.views.mixins import BaseListViewMixin, BaseLoginRequiredMixin
from notes.models import Note
from notes.forms import NoteForm
from notes.filters import NotesFilter
from manager.views.mixins import ManagerAccessMixin


class NoteListView(BaseLoginRequiredMixin, ManagerAccessMixin, BaseListViewMixin, ListView):
    template_name = "notes/list.html"
    model = Note
    http_method_names = ["get"]
    paginate_by = LIST_VIEW_PAGINATE_BY

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", get_trans_txt("All notes"))
        context.setdefault("filter_form", self.filterset.form)
        context.setdefault("page_header", "clients contacts".title())
        # print(self.filterset.form["contact_name"])
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = NotesFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs


class NoteCreateView(
    BaseLoginRequiredMixin,
    ManagerAccessMixin,
    SuccessMessageMixin,
    BaseListViewMixin,
    CreateView,
):
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
        kwargs.update({"created_by": self.request.user})
        if client_pk is not None:
            kwargs.update({"client_pk": client_pk})
        return kwargs


class NotesUpdateView(
    BaseLoginRequiredMixin,
    ManagerAccessMixin,
    SuccessMessageMixin,
    BaseListViewMixin,
    UpdateView,
):
    template_name = "notes/update.html"
    model = Note
    http_method_names = ["get", "post"]
    form_class = NoteForm
    success_message = get_trans_txt("Note update successfully")
    success_url = reverse_lazy("notes:list")

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        important_contact = self.get_object()
        context.setdefault("title", get_trans_txt("Update note"))
        return context


class NoteDeleteView(
    BaseLoginRequiredMixin,
    ManagerAccessMixin,
    SuccessMessageMixin,
    BaseListViewMixin,
    DeleteView,
):
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
