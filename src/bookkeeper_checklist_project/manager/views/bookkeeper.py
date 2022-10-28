from bookkeeper.models import Bookkeeper
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from jobs.forms import JobForm

from .mixins import ManagerAccessMixin


class BookkeepersListView(LoginRequiredMixin, ManagerAccessMixin, ListView):
    login_url = reverse_lazy("users:login")
    template_name: str = "manager/bookkeeper/list.html"
    model = Bookkeeper
    # paginate_by: int = 10

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context["title"] = "All bookkeepers"
        return context


class BookkeepersDetailsView(LoginRequiredMixin, ManagerAccessMixin, DetailView):
    login_url = reverse_lazy("users:login")
    template_name = "manager/bookkeeper/details.html"
    model = Bookkeeper

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        bookkeeper_fullname = self.get_object().user.fullname
        context["title"] = f"{bookkeeper_fullname}"
        context["jobs_form"] = JobForm(bookkeeper=self.get_object())
        # print(context["jobs_form"].data)
        return context
