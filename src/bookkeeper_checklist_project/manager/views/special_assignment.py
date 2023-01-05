# -*- coding: utf-8 -*-#
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, CreateView, UpdateView

from core.utils import get_trans_txt
from special_assignment.forms import SpecialAssignmentForm
from special_assignment.models import SpecialAssignment
from .mixins import ManagerAccessMixin


class SpecialAssignmentListView(LoginRequiredMixin, ManagerAccessMixin, ListView):
    login_url = reverse_lazy("users:login")
    template_name = "manager/special_assignment/list.html"
    model = SpecialAssignment

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context["title"] = get_trans_txt("All special assignments")
        return context


class SpecialAssignmentCreateView(
    LoginRequiredMixin, ManagerAccessMixin, SuccessMessageMixin, CreateView
):
    login_url = reverse_lazy("users:login")
    template_name = "manager/special_assignment/create.html"
    form_class = SpecialAssignmentForm
    success_message = get_trans_txt("Special assignment created successfully!")
    model = SpecialAssignment
    success_url = reverse_lazy("manager:special_assignment:list")

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context["title"] = get_trans_txt("Create special assignment")
        return context

    def form_valid(self, form):
        start_date = form.cleaned_data.get("start_date")
        due_date = form.cleaned_data.get("due_date")
        if start_date > due_date:
            form.add_error("start_date", get_trans_txt("Start date bigger than due date!"))
            return self.form_invalid(form)

        return super().form_valid(form)


class SpecialAssignmentUpdateView(
    LoginRequiredMixin, ManagerAccessMixin, SuccessMessageMixin, UpdateView
):
    login_url = reverse_lazy("users:login")
    template_name = "manager/special_assignment/update.html"
    form_class = SpecialAssignmentForm
    success_message = get_trans_txt("Special assignment updated successfully!")
    model = SpecialAssignment
    success_url = reverse_lazy("manager:special_assignment:list")

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context["title"] = get_trans_txt("Update special assignment")
        return context

    def get_success_url(self):
        url = reverse_lazy(
            "manager:special_assignment:update", kwargs={"pk": self.get_object().pk}
        )
        return url


class SpecialAssignmentDeleteView(
    LoginRequiredMixin, ManagerAccessMixin, SuccessMessageMixin, DeleteView
):
    login_url = reverse_lazy("users:login")
    model = SpecialAssignment
    template_name = "manager/special_assignment/delete.html"
    success_message: str = get_trans_txt("Special assignment deleted successfully!")
    success_url = reverse_lazy("manager:special_assignment:list")
