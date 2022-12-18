# -*- coding: utf-8 -*-#

import traceback

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView

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

    def get_queryset(self):
        try:
            bookkeeper = self.request.user.bookkeeper_related.get()
            jobs_list = []
            jobs = Job.objects.all()
            for job in jobs:
                # check if the bookkeeper in the job bookkeepers
                if bookkeeper in job.bookkeeper.filter():
                    jobs_list.append(job.pk)
            jobs = Job.objects.select_related().filter(pk__in=jobs_list)
            return jobs
        except Exception as ex:
            logger.error(traceback.format_exc())
            raise Exception(str(ex))


class JobDetailView(
    LoginRequiredMixin, BookkeeperAccessMixin, UserPassesTestMixin, DetailView
):
    login_url = reverse_lazy("login")
    template_name = "bookkeeper/jobs/detail.html"
    model = Job

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        job = self.get_object()
        context.setdefault("title", f"Job - {job.title}")

        return context

    def test_func(self) -> bool | None:
        job = self.get_object()
        bookkeepers_list = []
        bookkeeper = self.request.user.bookkeeper_related.get()
        for book_keeper in job.bookkeeper.filter():
            bookkeepers_list.append(book_keeper)
        if bookkeeper in bookkeepers_list:
            return True
        else:
            return False
