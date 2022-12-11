# -*- coding: utf-8 -*-#
import traceback

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView

from client.models import Client
from core.utils import get_formatted_logger
from jobs.models import Job
from .mixins import BookkeeperAccessMixin

logger = get_formatted_logger(__file__)


class JobListView(LoginRequiredMixin, BookkeeperAccessMixin, ListView):
    login_url = reverse_lazy("login")
    template_name = "bookkeeper/jobs/list.html"
    model = Job

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", "All Jobs")

        return context


class JobDetailView(LoginRequiredMixin, BookkeeperAccessMixin, DetailView):
    login_url = reverse_lazy("login")
    template_name = "bookkeeper/jobs/detail.html"
    model = Job

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", "Job - ")

        return context
