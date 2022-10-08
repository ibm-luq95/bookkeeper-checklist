from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.views import redirect_to_login
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect


class AssistantAccessMixin(PermissionRequiredMixin):
    permission_required = "assistant.assistant_user"

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect_to_login(
                self.request.get_full_path(),
                self.get_login_url(),
                self.get_redirect_field_name(),
            )

        if not self.has_permission():
            user_type = self.request.user.user_type
            raise PermissionDenied

        return super(AssistantAccessMixin, self).dispatch(request, *args, **kwargs)
