import traceback

import faker
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView

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


class ClientsDetailsView(LoginRequiredMixin, BookkeeperAccessMixin, DetailView):
    template_name = "bookkeeper/clients/details.html"
    login_url = reverse_lazy("users:login")
    model = Client

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", self.get_object().name)
        acc_and_services = list()
        fake = faker.Faker()
        for _ in range(35):
            acc_and_services.append(
                {
                    "id": fake.pyint(),
                    "url": fake.url(),
                    "username": fake.user_name(),
                    "password": fake.password(),
                }
            )
        context.setdefault("fake_data", acc_and_services)
        return context
