from typing import Optional

from betterforms.multiform import MultiModelForm
from django import forms
from django.contrib.auth.models import Permission
from django.db import transaction
from django.utils.safestring import mark_safe

from bookkeeper.models import Bookkeeper
from client.models import Client, ClientProxy
from core.forms import BaseModelFormMixin, SaveCreatedByFormMixin
from core.utils import debugging_print
from important_contact.forms import ImportantContactForm
from users.models import CustomUser


class ClientForm(BaseModelFormMixin, SaveCreatedByFormMixin):
    def __init__(
        self, created_by=None, user: Optional[CustomUser] = None, *args, **kwargs
    ):
        super(ClientForm, self).__init__(*args, **kwargs)
        self.fields.pop("is_active")

        if created_by is not None:
            self.created_by = created_by
        if user:
            if user.user_type == "assistant":
                check_permission = user.has_perm(
                    "assistant.can_assign_bookkeeper_to_client"
                )
                if check_permission is False:
                    self.fields.get("bookkeepers").widget.attrs.setdefault(
                        "disabled", "disabled"
                    )
                    help_txt = "<strong class='has-text-danger'>**You dont have permission to assign bookkeeper to this client,contact administrator for more details **</strong>"

                    self.fields.get("bookkeepers").help_text = mark_safe(help_txt)

    class Meta(BaseModelFormMixin.Meta):
        model = ClientProxy
        # fields = "__all__"
        widgets = {
            "bookkeepers": forms.CheckboxSelectMultiple(),
            "important_contacts": forms.CheckboxSelectMultiple(),
        }

    def save(self, commit=True):
        # Save the provided password in hashed format
        client = super().save(commit=False)
        with transaction.atomic():
            if commit:
                client.save()
            self.save_m2m()
            return client
