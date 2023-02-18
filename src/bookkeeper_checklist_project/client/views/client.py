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

from client.filters import ClientFilter
from client.forms import ClientForm
from client.models import Client
from company_services.forms import CompanyServiceForm
from core.constants import LIST_VIEW_PAGINATE_BY
from core.constants.status_labels import CON_ARCHIVED
from core.utils import get_trans_txt
from core.views.mixins import BaseListViewMixin, BaseLoginRequiredMixin
from documents.forms import DocumentForm
from important_contact.forms import ImportantContactForm
from jobs.forms import JobForm
from manager.views.mixins import ManagerAccessMixin, ManagerAssistantAccessMixin
from notes.forms import NoteForm
from special_assignment.forms import SpecialAssignmentForm
from task.forms import TaskForm


class ClientListView(
    BaseLoginRequiredMixin,
    PermissionRequiredMixin,
    ManagerAssistantAccessMixin,
    BaseListViewMixin,
    ListView,
):
    permission_required = "client.can_view_list"
    template_name = "client/list.html"
    model = Client
    # queryset = Client.objects.filter(~Q(status="archive")).prefetch_related("jobs")
    queryset = Client.objects.prefetch_related(
        "jobs", "jobs__created_by", "important_contacts"
    ).filter(~Q(status=CON_ARCHIVED))
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


class ClientArchiveListView(
    BaseLoginRequiredMixin,
    PermissionRequiredMixin,
    ManagerAssistantAccessMixin,
    BaseListViewMixin,
    ListView,
):
    permission_required = "client.view_archive"
    template_name = "client/list.html"
    model = Client
    queryset = Client.objects.prefetch_related("jobs").filter(Q(status=CON_ARCHIVED))
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


class ClientCreateView(
    BaseLoginRequiredMixin,
    PermissionRequiredMixin,
    ManagerAssistantAccessMixin,
    SuccessMessageMixin,
    BaseListViewMixin,
    CreateView,
):
    permission_required = "client.add_client"
    template_name = "client/create.html"
    form_class = ClientForm
    success_message = get_trans_txt("Client created successfully")
    success_url = reverse_lazy("client:list")

    # template_name_suffix = "_create_client"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", get_trans_txt("Create client"))
        return context

    def get_form_kwargs(self):
        kwargs = super(ClientCreateView, self).get_form_kwargs()
        kwargs.update({"created_by": self.request.user})
        return kwargs


class ClientDetailsView(
    BaseLoginRequiredMixin, PermissionRequiredMixin, ManagerAssistantAccessMixin, DetailView
):
    template_name = "client/details.html"
    model = Client
    permission_required = "client.view_client"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        client = self.get_object()
        important_contacts = client.important_contacts.filter().select_related()
        context.setdefault("title", f"Client - {client.name}")
        # important_contact_form = ImportantContactForm(
        #     instance=client.important_contact, is_readonly=False
        # )  # OLD, Before refactoring the important contact
        important_contact_form = ImportantContactForm()
        special_assignment_form = SpecialAssignmentForm(
            assigned_by=self.request.user, initial={"client": client}
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
        context.setdefault("special_assignment_form", special_assignment_form)
        # context.setdefault("important_contacts", important_contacts)
        origin = self.request.get_host()
        context.setdefault("origin", origin)
        return context


class ClientDetailsOverviewRedirectView(
    BaseLoginRequiredMixin,
    PermissionRequiredMixin,
    ManagerAssistantAccessMixin,
    RedirectView,
):
    pattern_name = "client:details:overview"
    permission_required = "client.view_client"


class ClientUpdateView(
    BaseLoginRequiredMixin,
    PermissionRequiredMixin,
    ManagerAssistantAccessMixin,
    SuccessMessageMixin,
    UpdateView,
):
    permission_required = "client.change_client"
    template_name = "client/update.html"
    model = Client
    template_name_suffix = "_update_form"
    form_class = ClientForm
    success_url = reverse_lazy("client:list")
    success_message = "Client update successfully"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context["title"] = "Update client"
        # important_contact_form = ImportantContactForm(
        #     instance=self.get_object().important_contact
        # )
        # context.setdefault("important_contact_form", important_contact_form)
        return context


class ClientDeleteView(
    BaseLoginRequiredMixin,
    PermissionRequiredMixin,
    ManagerAssistantAccessMixin,
    SuccessMessageMixin,
    DeleteView,
):
    model = Client
    permission_required = "client.delete_client"
    template_name = "client/delete.html"
    success_message: str = "Client deleted successfully!"
    success_url = reverse_lazy("client:list")
