from typing import List, Optional

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from prettyprinter import cpprint
from termcolor import cprint

from users.forms import CustomUserLoginForm


class LoginView(SuccessMessageMixin, FormView):
    http_method_names = ["post", "get"]
    success_url = reverse_lazy("users:login")
    template_name = "users/login.html"
    form_class = CustomUserLoginForm
    success_message: str = "Login successfully"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context["title"] = "Login"
        return context

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.

        user_type = form.cleaned_data.get("user_type")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, email=email, password=password)
        # sogeka@mailinator.com
        if user is not None:
            login(self.request, user)
        else:
            messages.error(self.request, "User credentials not correct!")
            return super().form_invalid(form)
        print("######################")
        print(user.user_type)
        print("######################")
        if user_type == "assistant":
            return redirect("assistant:assistant-dashboard")
        elif user_type == "bookkeeper":
            return redirect("bookkeeper:bookkeeper-dashboard")
        elif user_type == "manager":
            return redirect("manager:dashboard")

        # messages.success(self.request, "Login Success")
        return super().form_valid(form)
