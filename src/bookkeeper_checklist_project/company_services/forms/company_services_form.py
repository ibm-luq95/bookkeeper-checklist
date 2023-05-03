from django import forms

from company_services.helpers import PasswordHasher
from company_services.models import CompanyService
from core.forms import BaseModelFormMixin, SaveCreatedByFormMixin
from core.forms.widgets import CustomPasswordInputWidget


class CompanyServiceForm(BaseModelFormMixin, SaveCreatedByFormMixin):
    def __init__(
        self,
        client=None,
        is_update=False,
        updated_object=None,
        created_by=None,
        *args,
        **kwargs
    ):
        super(CompanyServiceForm, self).__init__(*args, **kwargs)
        # debugging_print(self.fields)
        self.fields.pop("status")
        self.is_update = is_update
        self.updated_object = updated_object
        if client is not None:
            self.fields["client"].initial = client
        if created_by is not None:
            self.created_by = created_by
        # if self.is_update is True:
        #     # pass
        #     self.initial["password"] = self.updated_object.decrypted_password

    password = forms.CharField(widget=CustomPasswordInputWidget, required=False)

    def clean_password(self):
        data = self.cleaned_data["password"]
        if self.is_update is True:
            # debugging_print("Update")
            if not data:
                # debugging_print("No password")
                data = PasswordHasher.encrypt(self.updated_object.decrypted_password)
            else:
                data = PasswordHasher.encrypt(data)
            # debugging_print(data)
        else:
            data = PasswordHasher.encrypt(data)
        # Always return a value to use as the new cleaned data, even if
        # this method didn't change it.

        return data

    class Meta(BaseModelFormMixin.Meta):
        model = CompanyService
