# -*- coding: utf-8 -*-#
from django.contrib.auth.mixins import LoginRequiredMixin
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

from client.filters import ClientFilter
from client.forms import ClientForm
from client.models import Client
from company_services.forms import CompanyServiceForm
from core.constants import LIST_VIEW_PAGINATE_BY
from core.utils import get_trans_txt
from core.views.mixins import BaseListViewMixin
from documents.forms import DocumentForm
from important_contact.forms import ImportantContactForm
from jobs.forms import JobForm
from manager.views.mixins import ManagerAccessMixin
from notes.forms import NoteForm
from task.forms import TaskForm


class ManagerClientListView(
    LoginRequiredMixin, ManagerAccessMixin, BaseListViewMixin, ListView
):
    login_url = reverse_lazy("users:auth:login")
    template_name = "client/list.html"
    model = Client
    # queryset = Client.objects.filter(~Q(status="archive")).prefetch_related("jobs")
    queryset = Client.objects.prefetch_related(
        "jobs", "jobs__created_by", "important_contacts"
    ).filter(~Q(status="archive"))
    paginate_by = LIST_VIEW_PAGINATE_BY
    list_type = "list"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context["title"] = get_trans_txt("All clients")
        context.setdefault("filter_form", self.filterset.form)
        context.setdefault("list_type", self.list_type)
        context.setdefault("page_header", "all clients".title())

        # debugging_print(self.filterset.form["name"])
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ClientFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs


class ManagerClientArchiveListView(
    LoginRequiredMixin, ManagerAccessMixin, BaseListViewMixin, ListView
):
    login_url = reverse_lazy("users:auth:login")
    template_name = "client/list.html"
    model = Client
    queryset = Client.objects.prefetch_related("jobs").filter(Q(status="archive"))
    paginate_by = LIST_VIEW_PAGINATE_BY
    list_type = "archive"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", get_trans_txt("All archived clients"))
        context.setdefault("filter_form", self.filterset.form)
        context.setdefault("list_type", self.list_type)
        context.setdefault("page_header", "archived clients".title())
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ClientFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs


class ManagerClientCreateView(
    LoginRequiredMixin,
    SuccessMessageMixin,
    ManagerAccessMixin,
    BaseListViewMixin,
    CreateView,
):
    login_url = reverse_lazy("users:auth:login")
    template_name = "client/create.html"
    form_class = ClientForm
    success_message = get_trans_txt("Client created successfully")
    success_url = reverse_lazy("client:manager:list")

    # template_name_suffix = "_create_client"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", get_trans_txt("Create client"))
        return context

    def get_form_kwargs(self):
        kwargs = super(ManagerClientCreateView, self).get_form_kwargs()
        kwargs.update({"created_by": self.request.user})
        return kwargs

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save()
        important_contacts = form.cleaned_data.get("important_contacts")
        if important_contacts:
            for contact in important_contacts:
                self.object.important_contacts.add(contact)
            self.object.save()
        return super().form_valid(form)


class ManagerClientDetailsView(LoginRequiredMixin, ManagerAccessMixin, DetailView):
    login_url = reverse_lazy("users:auth:login")
    template_name = "client/details.html"
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
        company_services_form = CompanyServiceForm(initial={"client": client})
        jobs_form = JobForm(initial={"client": client})
        tasks_form = TaskForm(initial={"client": client})
        context.setdefault("important_contact_form", important_contact_form)
        document_form = DocumentForm(
            initial={"document_section": "client", "client": client}
        )
        note_form = NoteForm(initial={"note_section": "client", "client": client})
        context.setdefault("document_form", document_form)
        context.setdefault("note_form", note_form)
        context.setdefault("company_services_form", company_services_form)
        context.setdefault("jobs_form", jobs_form)
        context.setdefault("tasks_form", tasks_form)
        # context.setdefault("important_contacts", important_contacts)
        origin = self.request.get_host()
        context.setdefault("origin", origin)
        return context


class ManagerClientDetailsOverviewRedirectView(
    LoginRequiredMixin, ManagerAccessMixin, RedirectView
):
    pattern_name = "client:manager:details:overview"


class ManagerClientUpdateView(
    LoginRequiredMixin,
    ManagerAccessMixin,
    SuccessMessageMixin,
    UpdateView,
):
    login_url = reverse_lazy("users:auth:login")
    template_name = "client/update.html"
    model = Client
    template_name_suffix = "_update_form"
    form_class = ClientForm
    success_url = reverse_lazy("client:manager:list")
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

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save()
        important_contacts = form.cleaned_data.get("important_contacts")
        if important_contacts:
            for contact in important_contacts:
                self.object.important_contacts.add(contact)
            self.object.save()
        return super().form_valid(form)


class ManagerClientDeleteView(
    LoginRequiredMixin,
    ManagerAccessMixin,
    SuccessMessageMixin,
    DeleteView,
):
    login_url = reverse_lazy("users:auth:login")
    model = Client
    template_name = "client/delete.html"
    success_message: str = "Client deleted successfully!"
    success_url = reverse_lazy("client:manager:list")