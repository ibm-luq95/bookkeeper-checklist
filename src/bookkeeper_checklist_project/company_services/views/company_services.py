# -*- coding: utf-8 -*-#
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, CreateView, UpdateView

from company_services.filters import CompanyServicesFilter
from company_services.forms import CompanyServiceForm
from company_services.models import CompanyService
from core.constants import LIST_VIEW_PAGINATE_BY
from core.utils import get_trans_txt
from core.views.mixins import BaseListViewMixin, BaseLoginRequiredMixin
from manager.views.mixins import ManagerAccessMixin, ManagerAssistantAccessMixin


class CompanyServicesListView(
    BaseLoginRequiredMixin,
    PermissionRequiredMixin,
    ManagerAssistantAccessMixin,
    BaseListViewMixin,
    ListView,
):
    permission_required = "company_services.can_view_list"
    template_name = "company_services/list.html"
    model = CompanyService
    http_method_names = ["get"]
    list_type = "list"
    paginate_by = LIST_VIEW_PAGINATE_BY

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", get_trans_txt("Company Services"))
        context.setdefault("page_header", "company and services".capitalize())
        context.setdefault("list_type", self.list_type)
        context.setdefault("filter_form", self.filterset.form)
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = CompanyServicesFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    # def get_queryset(self) -> BaseQuerySetMixin:
    #     """
    #     Return the list of items for this view.
    #     The return value must be an iterable and may be an instance of
    #     `QuerySet` in which case `QuerySet` specific behavior will be enabled.
    #     """
    #     queryset = super(CompanyServicesListView, self).get_queryset()
    #     queryset = CompanyService.objects.select_related().only("email", "client", "service_name", "label")
    #     return queryset


class CompanyServicesCreateView(
    BaseLoginRequiredMixin,
    ManagerAssistantAccessMixin,
    PermissionRequiredMixin,
    SuccessMessageMixin,
    BaseListViewMixin,
    CreateView,
):
    permission_required = "company_services.add_companyservice"
    template_name = "company_services/create.html"
    model = CompanyService
    http_method_names = ["get", "post"]
    form_class = CompanyServiceForm
    success_message = get_trans_txt("Company service created successfully")
    success_url = reverse_lazy("company_services:list")

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context["title"] = get_trans_txt("Create company services")
        return context

    def get_form_kwargs(self):
        kwargs = super(CompanyServicesCreateView, self).get_form_kwargs()
        kwargs.update({"created_by": self.request.user})
        return kwargs


class CompanyServicesDeleteView(
    BaseLoginRequiredMixin,
    ManagerAssistantAccessMixin,
    PermissionRequiredMixin,
    SuccessMessageMixin,
    BaseListViewMixin,
    DeleteView,
):
    permission_required = "company_services.delete_companyservice"
    model = CompanyService
    template_name = "company_services/delete.html"
    success_message: str = get_trans_txt("Company service deleted successfully!")
    success_url = reverse_lazy("company_services:list")


class CompanyServicesUpdateView(
    BaseLoginRequiredMixin,
    ManagerAssistantAccessMixin,
    PermissionRequiredMixin,
    SuccessMessageMixin,
    BaseListViewMixin,
    UpdateView,
):
    permission_required = "company_services.change_companyservice"
    template_name = "company_services/update.html"
    model = CompanyService
    http_method_names = ["get", "post"]
    form_class = CompanyServiceForm
    success_message = get_trans_txt("Company service updated successfully")
    success_url = reverse_lazy("company_services:list")

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        company_service = self.get_object()
        context["title"] = get_trans_txt(f"Update service to {company_service.client}")
        return context

    def get_form_kwargs(self):
        kwargs = super(CompanyServicesUpdateView, self).get_form_kwargs()
        kwargs.update({"is_update": True, "updated_object": self.get_object()})
        return kwargs

    # def form_valid(self, form):
    #     """If the form is valid, save the associated model."""
    #     self.object = form.save()
    #     if not form.data.get("password"):
    #         self.object.password = PasswordHasher.encrypt(self.object.decrypted_password)
    #     self.object.save()
    #     return super().form_valid(form)
