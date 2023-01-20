# -*- coding: utf-8 -*-#
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from client.filters import ClientFilter
from client.forms import ClientForm
from client.models import Client
from company_services.forms import CompanyServiceForm
from core.utils import get_trans_txt
from documents.forms import DocumentForm
from important_contact.forms import ImportantContactForm
from jobs.forms import JobForm
from notes.forms import NoteForm
from task.forms import TaskForm
from .mixins import ManagerAccessMixin


class ClientListView(LoginRequiredMixin, ManagerAccessMixin, ListView):
    login_url = reverse_lazy("users:login")
    template_name = "manager/client/list.html"
    model = Client
    queryset = Client.objects.select_related().filter(~Q(status="archive"))

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context["title"] = get_trans_txt("All clients")
        context.setdefault("filter_form", self.filterset.form)
        # debugging_print(self.filterset.form["name"])
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ClientFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs


class ClientArchiveListView(LoginRequiredMixin, ManagerAccessMixin, ListView):
    login_url = reverse_lazy("users:login")
    template_name = "manager/client/archive_list.html"
    model = Client
    queryset = Client.objects.select_related().filter(Q(status="archive"))

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context["title"] = get_trans_txt("All archived clients")
        return context


class ClientCreateView(
    LoginRequiredMixin, SuccessMessageMixin, ManagerAccessMixin, CreateView
):
    login_url = reverse_lazy("users:login")
    template_name = "manager/client/create.html"
    form_class = ClientForm
    success_message = "Client created successfully"
    success_url = reverse_lazy("manager:client:list")

    # template_name_suffix = "_create_client"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", get_trans_txt("Create client"))
        return context

    # def form_valid(self, form):
    #     """If the form is valid, save the associated model."""
    #     self.object = form.save()
    #     # Save the user first, because the profile needs a user before it
    #     # can be saved.
    #     client = form["client"].save(commit=False)
    #     important_contact = form["important_contact"].save()
    #     client.important_contact = important_contact
    #     client.save()
    #     return super().form_valid(form)


class ClientDetailView(LoginRequiredMixin, ManagerAccessMixin, DetailView):
    login_url = reverse_lazy("users:login")
    template_name = "manager/client/details.html"
    model = Client

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        client = self.get_object()
        important_contacts = client.important_contacts.filter().select_related()
        context.setdefault("title", f"Client - {client.name}")
        # important_contact_form = ImportantContactForm(
        #     instance=client.important_contact, is_readonly=False
        # )  # OLD, Before refactoring the important contact
        important_contact_form = ImportantContactForm(
            is_readonly=True, remove_client_field=True
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
        # context.setdefault("important_contacts", important_contacts)
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
    form_class = ClientForm
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

    # def get_form_kwargs(self):
    #     kwargs = super(ClientUpdateView, self).get_form_kwargs()
    #     kwargs.update(
    #         instance={
    #             "client": self.object,
    #             "important_contact": self.object.important_contact,
    #         }
    #     )
    #     return kwargs


class ClientDeleteView(
    LoginRequiredMixin, ManagerAccessMixin, SuccessMessageMixin, DeleteView
):
    login_url = reverse_lazy("users:login")
    model = Client
    template_name = "manager/client/delete.html"
    success_message: str = "Client deleted successfully!"
    success_url = reverse_lazy("manager:client:list")
