import random
from datetime import datetime

import faker
import requests
from core.models import Quote
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from prettyprinter import cpprint

from .mixins import BookkeeperAccessMixin


class ClientsListView(LoginRequiredMixin, BookkeeperAccessMixin, TemplateView):
    template_name = "bookkeeper/clients/list.html"
    login_url = reverse_lazy("users:login")

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", "All Clients")
        cpprint(self.request.user.groups.all())
        return context


class ClientsDetailsView(LoginRequiredMixin, BookkeeperAccessMixin, TemplateView):
    template_name = "bookkeeper/clients/details.html"
    login_url = reverse_lazy("users:login")

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", "Client Details")
        acc_and_services = list()
        fake = faker.Faker()
        for _ in range(35):
            acc_and_services.append({
                "id": fake.pyint(),
                "url": fake.url(),
                "username": fake.user_name(),
                "password": fake.password()
            })
        context.setdefault("fake_data", acc_and_services)
        return context
