import traceback

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView

from client.models import Client
from core.utils import get_formatted_logger
from jobs.models import Job
from .mixins import BookkeeperAccessMixin

logger = get_formatted_logger(__file__)


class ClientsListView(LoginRequiredMixin, BookkeeperAccessMixin, ListView):
    template_name = "bookkeeper/clients/list.html"
    login_url = reverse_lazy("users:login")
    model = Client

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", "All Clients")
        bookkeeper = self.request.user.bookkeeper_related.get()
        # cpprint(self.request.user.groups.all())
        # cpprint(self.request.user.bookkeeper_related.get())

        return context

    def get_queryset(self):
        try:
            bookkeeper = self.request.user.bookkeeper_related.get()
            jobs = Job.objects.all()
            jobs_queryset = jobs.filter(bookkeeper=bookkeeper).values_list("client")
            jobs_queryset = [pk[0] for pk in jobs_queryset]
            queryset = Client.objects.filter(pk__in=jobs_queryset)
            return queryset
        except Exception as ex:
            logger.error(traceback.format_exc())
            raise Exception(str(ex))


class ClientsDetailsView(
    LoginRequiredMixin, BookkeeperAccessMixin, UserPassesTestMixin, DetailView
):
    template_name = "bookkeeper/clients/details.html"
    login_url = reverse_lazy("users:login")
    model = Client

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", self.get_object().name)
        return context

    def test_func(self) -> bool | None:
        bookkeepers_list = []
        client = self.get_object()
        bookkeeper = self.request.user.bookkeeper_related.get()
        for job in client.jobs.filter():
            for bookk in job.bookkeeper.filter():
                bookkeepers_list.append(bookk)
        if bookkeeper in bookkeepers_list:
            return True
        else:
            return False
