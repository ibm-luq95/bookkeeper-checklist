# -*- coding: utf-8 -*-#
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, CreateView, UpdateView

from company_services.forms import CompanyServiceForm
from company_services.models import CompanyService
from core.utils import get_trans_txt
from .mixins import ManagerAccessMixin


class CompanyServicesListView(LoginRequiredMixin, ManagerAccessMixin, ListView):
    login_url = reverse_lazy("users:login")
    template_name = "manager/company_service/list.html"
    model = CompanyService
    http_method_names = ["get"]

    # queryset = CompanyService.objects.all().values("pk", "email", "client", "service_name", "label", "url")
    # queryset = CompanyService.objects.prefetch_related("client").only("password").values("pk", "client", "label", "url", "service_name")

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context["title"] = get_trans_txt("Company Services")
        return context

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
    LoginRequiredMixin, ManagerAccessMixin, SuccessMessageMixin, CreateView
):
    login_url = reverse_lazy("users:login")
    template_name = "manager/company_service/create.html"
    model = CompanyService
    http_method_names = ["get", "post"]
    form_class = CompanyServiceForm
    success_message = get_trans_txt("Company service created successfully")
    success_url = reverse_lazy("manager:company_services:list")

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context["title"] = get_trans_txt("Create company services")
        return context


class CompanyServicesDeleteView(
    LoginRequiredMixin, ManagerAccessMixin, SuccessMessageMixin, DeleteView
):
    login_url = reverse_lazy("users:login")
    model = CompanyService
    template_name = "manager/company_service/delete.html"
    success_message: str = get_trans_txt("Company service deleted successfully!")
    success_url = reverse_lazy("manager:company_services:list")


class CompanyServicesUpdateView(
    LoginRequiredMixin, ManagerAccessMixin, SuccessMessageMixin, UpdateView
):
    login_url = reverse_lazy("users:login")
    template_name = "manager/company_service/update.html"
    model = CompanyService
    http_method_names = ["get", "post"]
    form_class = CompanyServiceForm
    success_message = get_trans_txt("Company service updated successfully")
    success_url = reverse_lazy("manager:company_services:list")

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
