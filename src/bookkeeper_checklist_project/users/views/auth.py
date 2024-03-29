# -*- coding: utf-8 -*-#
from decouple import config
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.edit import FormView

from core.cache import CacheViewMixin
from core.utils import get_trans_txt
from users.forms import CustomUserLoginForm
from users.models import CustomUser


class LoginView(SuccessMessageMixin, CacheViewMixin, FormView):
    http_method_names = ["post", "get"]
    success_url = reverse_lazy("users:auth:login")
    template_name = "users/login.html"
    form_class = CustomUserLoginForm
    success_message: str = get_trans_txt("Login successfully")

    def get(self, request, *args, **kwargs):
        """Handle GET requests: instantiate a blank version of the form."""
        if self.request.GET.get("next"):
            self.request.session.setdefault("next", self.request.GET.get("next"))
        # check if user authenticated
        if self.request.user.is_authenticated:
            user_type = self.request.user.user_type
            if user_type == "bookkeeper":
                return redirect("bookkeeper:dashboard")
            elif user_type == "manager":
                return redirect("manager:dashboard")
            elif user_type == "assistant":
                return redirect("assistant:dashboard")
        return self.render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", get_trans_txt("Login"))

        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        environment = config("STAGE_ENVIRONMENT", cast=str)
        if environment == "DEV" or environment == "STAGE":
            kwargs.update({"initial": {"user_type": "manager"}})
        return kwargs

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        user_type = form.cleaned_data.get("user_type")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")

        user_check = CustomUser.objects.filter(email=email)
        if not user_check:
            form.add_error("email", f"Email not exists!")
            return self.form_invalid(form)
            # raise ValidationError(f"Email not exists!", code="invalid")
        user_check = user_check.first()
        check_user_type = user_check.user_type

        # check if the user type came from the form equal the user type saved in the db
        if user_type != check_user_type:
            form.add_error("user_type", f"User type not matched your account type!")
            return self.form_invalid(form)
        user = authenticate(self.request, email=email, password=password)
        if user is not None:
            login(self.request, user)
        else:
            messages.error(self.request, "User credentials not correct!")
            return super().form_invalid(form)

        # Check if next url exists
        next_url = self.request.session.get("next", None)  # TODO: added to the end
        if next_url:
            return redirect(next_url)

        site_settings_object = self.cmx_get_item("web_app_settings")
        if user_type == "assistant":
            # check if assistants allowed to log in from site settings
            if site_settings_object.can_assistants_login is False:
                messages.error(
                    self.request,
                    "Assistants not allowed to login, contact the administrator",
                )
                logout(self.request)
                return super().form_invalid(form)
            else:
                return redirect("assistant:dashboard")

        elif user_type == "bookkeeper":
            # check if bookkeeper allowed to log in from site settings
            if site_settings_object.can_bookkeepers_login is False:
                messages.error(
                    self.request,
                    "Bookkeepers not allowed to login, contact the administrator",
                )
                logout(self.request)
                return super().form_invalid(form)
            else:
                return redirect("bookkeeper:dashboard")
        elif user_type == "manager":
            return redirect("manager:dashboard")

        return super().form_valid(form)
