from django.contrib.auth.views import redirect_to_login
from django.shortcuts import redirect
from django.contrib.auth.mixins import PermissionRequiredMixin


class ManagerAccessMixin(PermissionRequiredMixin):
    permission_required = "manager.manager_user"

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect_to_login(
                self.request.get_full_path(),
                self.get_login_url(),
                self.get_redirect_field_name(),
            )

        if not self.has_permission():
            user_type = self.request.user.user_type
            if user_type == "assistant":
                return redirect("assistant:assistant-dashboard")
            elif user_type == "bookkeeper":
                return redirect("bookkeeper:bookkeeper-dashboard")

        return super(ManagerAccessMixin, self).dispatch(request, *args, **kwargs)
