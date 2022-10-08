from django.views.generic.base import TemplateView
import faker
from core.models import Quote
import requests
from datetime import datetime
import random
from prettyprinter import cpprint


class ClientsListView(TemplateView):
    template_name = "bookkeeper/clients/list.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", "All Clients")
        return context


class ClientsDetailsView(TemplateView):
    template_name = "bookkeeper/clients/details.html"

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
