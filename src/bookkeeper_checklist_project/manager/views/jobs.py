# -*- coding: utf-8 -*-#
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView

from jobs.forms import JobForm
from jobs.models import Job
from task.forms import TaskForm
from .mixins import ManagerAccessMixin


class JobListView(LoginRequiredMixin, ManagerAccessMixin, ListView):
    login_url = reverse_lazy("users:login")
    template_name = "manager/jobs/list.html"
    model = Job

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context["title"] = "All jobs"
        return context


class JobCreateView(
    LoginRequiredMixin, ManagerAccessMixin, SuccessMessageMixin, CreateView
):
    # model = get_user_model()
    template_name = "manager/jobs/create.html"
    form_class = JobForm
    http_method_names = ["post", "get"]
    success_message: str = "Job created successfully"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context["title"] = "Create Job"
        return context


class JobDetailsView(LoginRequiredMixin, ManagerAccessMixin, DetailView):
    template_name = "manager/jobs/details.html"
    model = Job

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context["title"] = "Job details"
        context.setdefault("task_form", TaskForm)
        return context
