# -*- coding: utf-8 -*-#
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from bookkeeper.views.mixins import BookkeeperAccessMixin
from core.utils import get_trans_txt
from documents.forms import DocumentForm
from documents.models import Documents


class UpdateDocumentBookkeeperView(
    LoginRequiredMixin, BookkeeperAccessMixin, SuccessMessageMixin, UpdateView
):
    login_url = reverse_lazy("users:login")
    template_name = "bookkeeper/documents/update.html"
    form_class = DocumentForm
    success_message = get_trans_txt("Document updated successfully")
    model = Documents

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", "Update document")

        return context

    def get_success_url(self):
        url = reverse_lazy(
            "documents:bookkeeper:update", kwargs={"pk": self.get_object().pk}
        )
        return url

    def get_form_kwargs(self):
        """Return the keyword arguments for instantiating the form."""
        kwargs = super().get_form_kwargs()
        kwargs.update({"is_update": True})
        return kwargs
