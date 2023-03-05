# -*- coding: utf-8 -*-#
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy

from core.constants.status_labels import CON_COMPLETED, CON_ARCHIVED


class BaseListViewMixin:
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # debugging_print(dir(self.form_class))
        # debugging_print(self.form_class._meta.model._meta)
        context.setdefault("is_show_created_at", False)
        if hasattr(self.model, "_meta"):
            context.setdefault("app_label", self.model._meta.app_label)
            # context.setdefault("app_label", self.model._meta.model_name)
        return context


class BaseLoginRequiredMixin(LoginRequiredMixin):
    login_url = reverse_lazy("users:auth:login")


class DetailsViewMixin:
    def get_queryset(self):
        queryset = self.model.original_objects.filter(pk=self.kwargs.get("pk"))
        return queryset


class ListViewMixin:
    def get_queryset(self):
        queryset = self.model.objects.filter(~Q(status__in=[CON_COMPLETED, CON_ARCHIVED]))

        return queryset


class ArchiveListViewMixin:
    def get_queryset(self):
        queryset = self.model.objects.filter(Q(status__in=[CON_COMPLETED, CON_ARCHIVED]))
        return queryset
