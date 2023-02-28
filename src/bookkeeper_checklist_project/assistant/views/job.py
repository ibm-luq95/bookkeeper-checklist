# -*- coding: utf-8 -*-#
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from jobs.forms import JobForm
from jobs.models import Job
from core.utils import get_trans_txt
from .mixins import AssistantAccessMixin


class JobListView(LoginRequiredMixin, AssistantAccessMixin, ListView):
    template_name = "assistant/job/list.html"
    login_url = reverse_lazy("users:auth:login")
    model = Job

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", get_trans_txt("Jobs"))
        return context


class JobCreateView(
    LoginRequiredMixin, AssistantAccessMixin, SuccessMessageMixin, CreateView
):
    model = Job
    template_name = "assistant/job/create.html"
    form_class = JobForm
    http_method_names = ["post", "get"]
    success_message: str = get_trans_txt("Job created successfully")
    success_url = reverse_lazy("assistant:job:list")

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", get_trans_txt("Create job"))
        return context

    def get_form_kwargs(self):
        kwargs = super(JobCreateView, self).get_form_kwargs()
        kwargs.update({"created_by": self.request.user})
        return kwargs
