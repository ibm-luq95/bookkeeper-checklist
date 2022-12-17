# -*- coding: utf-8 -*-#
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ImproperlyConfigured
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from django.views.generic.edit import FormView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.urls import reverse_lazy
from client.models import Client
from core.utils import debugging_print
from .mixins import ManagerAccessMixin
from client.forms import ClientCreationMultiForm
from important_contact.forms import ImportantContactForm
from documents.forms import DocumentForm
from notes.forms import NoteForm
from company_services.forms import CompanyServiceForm
from jobs.forms import JobForm
from task.forms import TaskForm


class ClientListView(LoginRequiredMixin, ManagerAccessMixin, ListView):
    login_url = reverse_lazy("users:login")
    template_name = "manager/client/list.html"
    model = Client

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context["title"] = "All clients"
        return context


class ClientCreateView(
    LoginRequiredMixin, SuccessMessageMixin, ManagerAccessMixin, CreateView
):
    login_url = reverse_lazy("users:login")
    template_name = "manager/client/create.html"
    form_class = ClientCreationMultiForm
    success_message = "Client created successfully"
    success_url = reverse_lazy("manager:client:list")
    # template_name_suffix = "_create_client"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context["title"] = "Create client"
        return context

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save()
        # Save the user first, because the profile needs a user before it
        # can be saved.
        client = form["client"].save(commit=False)
        important_contact = form["important_contact"].save()
        client.important_contact = important_contact
        client.save()
        return super().form_valid(form)


class ClientDetailView(LoginRequiredMixin, ManagerAccessMixin, DetailView):
    login_url = reverse_lazy("users:login")
    template_name = "manager/client/details.html"
    model = Client

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        client = self.get_object()
        context["title"] = f"Client - {client.name}"
        important_contact_form = ImportantContactForm(
            instance=client.important_contact, is_readonly=False
        )
        company_services_form = CompanyServiceForm(client=client)
        jobs_form = JobForm(client=client)
        tasks_form = TaskForm(client=client)
        context.setdefault("important_contact_form", important_contact_form)
        document_form = DocumentForm(document_section="client", client=client)
        note_form = NoteForm(client=client, note_section="client")
        context.setdefault("document_form", document_form)
        context.setdefault("note_form", note_form)
        context.setdefault("company_services_form", company_services_form)
        context.setdefault("jobs_form", jobs_form)
        context.setdefault("tasks_form", tasks_form)
        origin = self.request.get_host()
        context.setdefault("origin", origin)
        return context


class ClientUpdateView(
    LoginRequiredMixin, ManagerAccessMixin, SuccessMessageMixin, UpdateView
):
    login_url = reverse_lazy("users:login")
    template_name = "manager/client/update.html"
    model = Client
    template_name_suffix = "_update_form"
    form_class = ClientCreationMultiForm
    success_url = reverse_lazy("manager:client:list")
    success_message = "Update successfully"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context["title"] = "Update client"
        # important_contact_form = ImportantContactForm(
        #     instance=self.get_object().important_contact
        # )
        # context.setdefault("important_contact_form", important_contact_form)
        return context

    def get_form_kwargs(self):
        kwargs = super(ClientUpdateView, self).get_form_kwargs()
        kwargs.update(
            instance={
                "client": self.object,
                "important_contact": self.object.important_contact,
            }
        )
        return kwargs


class ClientDeleteView(
    LoginRequiredMixin, ManagerAccessMixin, SuccessMessageMixin, DeleteView
):
    login_url = reverse_lazy("users:login")
    model = Client
    template_name = "manager/client/delete.html"
    success_message: str = "Client deleted successfully!"
    success_url = reverse_lazy("manager:client:list")
