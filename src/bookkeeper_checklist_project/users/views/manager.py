# -*- coding: utf-8 -*-#
from django.contrib.auth.models import Permission
from django.contrib.auth.views import PasswordChangeView
from django.contrib.contenttypes.models import ContentType
from django.contrib.messages.views import SuccessMessageMixin
from django.db import transaction
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, FormView

from core.cache import CacheViewMixin
from core.constants import LIST_VIEW_PAGINATE_BY
from core.utils import get_trans_txt, debugging_print
from core.views.mixins import BaseListViewMixin, BaseLoginRequiredMixin
from manager.views.mixins import ManagerAccessMixin
from django.forms.models import model_to_dict
from users.models import CustomUser
from users.forms import UserCreationForm, UserChangeForm, UserPasswordChangeForm
from users.filters import UsersFilter


class ManagerUsersListView(
    BaseLoginRequiredMixin, ManagerAccessMixin, BaseListViewMixin, ListView
):
    template_name = "users/list.html"
    model = CustomUser
    paginate_by = LIST_VIEW_PAGINATE_BY
    list_type = "list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.setdefault("list_type", self.list_type)
        context.setdefault("title", get_trans_txt("all users".capitalize()))
        context.setdefault("filter_form", self.filterset.form)
        context.setdefault("page_header", "users".capitalize())
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = UsersFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs


class ManagerUsersArchiveListView(
    BaseLoginRequiredMixin, ManagerAccessMixin, BaseListViewMixin, ListView
):
    template_name = "users/list.html"
    model = CustomUser
    paginate_by = LIST_VIEW_PAGINATE_BY
    list_type = "archive"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.setdefault("list_type", self.list_type)
        context.setdefault("title", get_trans_txt("all users".capitalize()))
        context.setdefault("filter_form", self.filterset.form)
        context.setdefault("page_header", "archived users".capitalize())
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = UsersFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs


class ManagerUsersCreateView(
    BaseLoginRequiredMixin,
    ManagerAccessMixin,
    SuccessMessageMixin,
    CreateView,
):
    template_name = "users/create.html"
    model = CustomUser
    form_class = UserCreationForm
    success_message = "User created successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.setdefault("title", get_trans_txt("create new user".capitalize()))
        return context

    def get_success_url(self):
        user_type = self.request.user.user_type
        url_pattern = f"users:{user_type}:list"
        url = reverse_lazy(url_pattern)
        return url


class ManagerUsersChangeView(
    BaseLoginRequiredMixin,
    ManagerAccessMixin,
    SuccessMessageMixin,
    UpdateView,
):
    template_name = "users/update.html"
    model = CustomUser
    form_class = UserChangeForm
    success_message = "User updated successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.setdefault(
            "title", f"update user {self.get_object().fullname}".capitalize()
        )
        return context

    def get_success_url(self):
        user_type = self.request.user.user_type
        url_pattern = f"users:{user_type}:list"
        url = reverse_lazy(url_pattern)
        return url

    def get_form_kwargs(self):
        kwargs = super(ManagerUsersChangeView, self).get_form_kwargs()

        kwargs.update(
            {
                "password_url": reverse_lazy(
                    "users:manager:update-password", kwargs={"pk": self.get_object().pk}
                ),
                "user_object": self.get_object(),
            }
        )
        return kwargs

    # def form_valid(self, form):
    #     self.object = form.save()
    #
    #     with transaction.atomic():
    #         if form.cleaned_data.get("user_permissions"):
    #             debugging_print(form.cleaned_data.get("user_permissions"))
    #
    #     return super().form_valid(form)


class ManagerUpdateUserPasswordView(
    BaseLoginRequiredMixin, ManagerAccessMixin, SuccessMessageMixin, UpdateView
):
    template_name = "users/update_password.html"
    form_class = UserPasswordChangeForm
    model = CustomUser
    success_url = "Password updated successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.setdefault("title", f"update {self.get_object().fullname} password".title())
        return context

    def get_form_kwargs(self):
        kwargs = super(ManagerUpdateUserPasswordView, self).get_form_kwargs()
        kwargs.update({"user": self.get_object()})
        return kwargs

    def get_success_url(self):
        user_type = self.request.user.user_type
        url_pattern = f"users:{user_type}:list"
        url = reverse_lazy(url_pattern)
        return url


class ManagerUsersDeleteView(
    BaseLoginRequiredMixin,
    ManagerAccessMixin,
    SuccessMessageMixin,
    DeleteView,
):
    template_name = "users/delete.html"
    model = CustomUser
    success_message = "User deleted successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.setdefault("title", get_trans_txt("delete user".capitalize()))
        return context

    def get_success_url(self):
        user_type = self.request.user.user_type
        url_pattern = f"users:{user_type}:list"
        url = reverse_lazy(url_pattern)
        return url
