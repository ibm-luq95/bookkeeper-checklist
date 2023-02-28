from django import forms

from client_account.models import ClientAccount
from company_services.helpers import PasswordHasher
from core.constants.form import EXCLUDED_FIELDS
from core.forms import BaseModelFormMixin, SaveCreatedByFormMixin
from core.forms.widgets import CustomPasswordInputWidget


class ClientAccountForm(BaseModelFormMixin, SaveCreatedByFormMixin):
    def __init__(
        self,
        client=None,
        is_update=False,
        updated_object=None,
        created_by=None,
        *args,
        **kwargs
    ):
        super(ClientAccountForm, self).__init__(*args, **kwargs)
        self.is_update = is_update
        self.updated_object = updated_object
        if client is not None:
            # print(self.fields.get("client"))
            self.fields["client"].initial = client

        if created_by is not None:
            self.created_by = created_by

    account_password = forms.CharField(widget=CustomPasswordInputWidget, required=False)

    def clean_account_password(self):
        data = self.cleaned_data["account_password"]
        if self.is_update is True:
            if not data:
                # debugging_print("No password")
                data = PasswordHasher.encrypt(
                    self.updated_object.decrypted_account_password
                )
            else:
                data = PasswordHasher.encrypt(data)
            # debugging_print(data)
        else:
            data = PasswordHasher.encrypt(data)
        # Always return a value to use as the new cleaned data, even if
        # this method didn't change it.

        return data

    class Meta(BaseModelFormMixin.Meta):
        model = ClientAccount
        exclude = EXCLUDED_FIELDS
