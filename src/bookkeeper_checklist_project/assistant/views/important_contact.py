# -*- coding: utf-8 -*-#
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, CreateView, UpdateView

from client.models import Client
from core.utils import get_trans_txt
from important_contact.filters import ImportantContactFilter
from important_contact.forms import ImportantContactForm
from important_contact.models import ImportantContact
from .mixins import AssistantAccessMixin


class ImportantContactListView(LoginRequiredMixin, AssistantAccessMixin, ListView):
    login_url = reverse_lazy("users:login")
    template_name = "assistant/important_contact/list.html"
    model = ImportantContact
    http_method_names = ["get"]

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context["title"] = get_trans_txt("All important contacts")
        context.setdefault("filter_form", self.filterset.form)
        # print(self.filterset.form["contact_name"])
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ImportantContactFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs


class ImportantContactCreateView(
    LoginRequiredMixin, AssistantAccessMixin, SuccessMessageMixin, CreateView
):
    login_url = reverse_lazy("users:login")
    template_name = "assistant/important_contact/create.html"
    model = ImportantContact
    http_method_names = ["get", "post"]
    form_class = ImportantContactForm
    success_message = get_trans_txt("Contact created successfully")

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
