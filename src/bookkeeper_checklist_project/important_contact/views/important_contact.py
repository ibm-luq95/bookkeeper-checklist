# -*- coding: utf-8 -*-#
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, CreateView, UpdateView

from client.models import Client
from core.constants import LIST_VIEW_PAGINATE_BY
from core.utils import get_trans_txt
from core.views.mixins import BaseListViewMixin, BaseLoginRequiredMixin
from important_contact.filters import ImportantContactFilter
from important_contact.forms import ImportantContactForm
from important_contact.models import ImportantContact
from manager.views.mixins import ManagerAccessMixin


class ImportantContactListView(
    BaseLoginRequiredMixin, ManagerAccessMixin, BaseListViewMixin, ListView
):
    template_name = "important_contact/list.html"
    model = ImportantContact
    http_method_names = ["get"]
    paginate_by = LIST_VIEW_PAGINATE_BY

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", get_trans_txt("All important contacts"))
        context.setdefault("filter_form", self.filterset.form)
        context.setdefault("page_header", "clients contacts".title())
        # print(self.filterset.form["contact_name"])
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ImportantContactFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs


class ImportantContactCreateView(
    BaseLoginRequiredMixin,
    ManagerAccessMixin,
    SuccessMessageMixin,
    BaseListViewMixin,
    CreateView,
):
    template_name = "important_contact/create.html"
    model = ImportantContact
    http_method_names = ["get", "post"]
    form_class = ImportantContactForm
    success_message = get_trans_txt("Contact created successfully")
    success_url = reverse_lazy("important_contact:list")

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        client_pk = self.request.GET.get("client")
        if client_pk is not None:
            client_obj = Client.objects.select_related().filter(pk=client_pk).first()
            context.setdefault("title", get_trans_txt(f"New contact for {client_obj.name}"))
        else:
            context.setdefault("title", get_trans_txt("Create new contact"))

        return context

    def get_form_kwargs(self):
        kwargs = super(ImportantContactCreateView, self).get_form_kwargs()
        client_pk = self.request.GET.get("client")
        kwargs.update({"created_by": self.request.user})
        if client_pk is not None:
            kwargs.update({"client_pk": client_pk})
        return kwargs

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save()
        client_pk = self.request.GET.get("client")
        if client_pk is not None:
            client_obj = Client.objects.select_related().filter(pk=client_pk).first()
            client_obj.important_contacts.add(self.object)
            client_obj.save()
        return super().form_valid(form)


class ImportantContactUpdateView(
    BaseLoginRequiredMixin,
    ManagerAccessMixin,
    SuccessMessageMixin,
    BaseListViewMixin,
    UpdateView,
):
    template_name = "important_contact/update.html"
    model = ImportantContact
    http_method_names = ["get", "post"]
    form_class = ImportantContactForm
    success_message = get_trans_txt("Contact update successfully")
    success_url = reverse_lazy("important_contact:list")

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        important_contact = self.get_object()
        context.setdefault(
            "title", get_trans_txt(f"Update contact to {important_contact.client}")
        )
        return context


class ImportantContactDeleteView(
    BaseLoginRequiredMixin,
    ManagerAccessMixin,
    SuccessMessageMixin,
    BaseListViewMixin,
    DeleteView,
):
    template_name = "important_contact/delete.html"
    model = ImportantContact
    http_method_names = ["get", "post"]
    success_message = get_trans_txt("Contact deleted successfully")
    success_url = reverse_lazy("important_contact:list")

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context["title"] = get_trans_txt("Delete")
        return context
