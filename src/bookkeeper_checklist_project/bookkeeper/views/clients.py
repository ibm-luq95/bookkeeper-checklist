import traceback

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView

from client.models import Client
from core.utils import get_formatted_logger
from important_contact.forms import ImportantContactForm
from jobs.models import Job
from .mixins import BookkeeperAccessMixin

logger = get_formatted_logger()


class ClientsListView(LoginRequiredMixin, BookkeeperAccessMixin, ListView):
    template_name = "bookkeeper/clients/list.html"
    login_url = reverse_lazy("users:auth:login")
    model = Client

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", "All Clients")
        bookkeeper = self.request.user.bookkeeper
        # cpprint(self.request.user.groups.all())
        # cpprint(self.request.user.bookkeeper.get())

        return context

    def get_queryset(self):
        try:
            bookkeeper = self.request.user.bookkeeper
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
    login_url = reverse_lazy("users:auth:login")
    model = Client
    http_method_names = ["get"]

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        client = self.get_object()
        important_contact_form = ImportantContactForm(
            is_readonly=True, remove_client_field=True
        )
        context.setdefault("title", client.name)
        context.setdefault("important_contact_form", important_contact_form)
        return context

    def test_func(self) -> bool:
        bookkeepers_list = []
        client = self.get_object()
        bookkeeper = self.request.user.bookkeeper
        special_assignments = bookkeeper.special_assignments.select_related().all()
        for job in client.jobs.filter():
            if hasattr(job, "bookkeeper"):
                for bookk in job.bookkeeper.filter():
                    bookkeepers_list.append(bookk)
        for sa in special_assignments:  # TODO: check if this correct to use
            bookkeepers_list.append(sa.get_managed_user())
        if bookkeeper in bookkeepers_list:
            return True
        else:
            return False
