# -*- coding: utf-8 -*-#
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.exceptions import ImproperlyConfigured
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from documents.forms import DocumentForm
from documents.models import Documents
from manager.views.mixins import ManagerAccessMixin


class CreateManagerDocumentView(
    LoginRequiredMixin, ManagerAccessMixin, SuccessMessageMixin, CreateView
):
    login_url = reverse_lazy("users:login")
    template_name = "manager/documents/create.html"
    form_class = DocumentForm
    success_message = "Document Created Successfully"

    def get_success_url(self):
        """Return the URL to redirect to after processing a valid form."""
        if self.success_url:
            url = self.success_url.format(**self.object.__dict__)
        else:
            try:
                url = self.object.get_absolute_url()
            except AttributeError:
                raise ImproperlyConfigured(
                    "No URL to redirect to.  Either provide a url or define"
                    " a get_absolute_url method on the Model."
                )
        return url


class ListManagerDocumentView(LoginRequiredMixin, ManagerAccessMixin, ListView):
    login_url = reverse_lazy("users:login")
    template_name = "manager/documents/list.html"
    model = Documents


class DetailsManagerDocumentView(LoginRequiredMixin, ManagerAccessMixin, DetailView):
    login_url = reverse_lazy("users:login")
    template_name = "manager/documents/show.html"
    model = Documents
