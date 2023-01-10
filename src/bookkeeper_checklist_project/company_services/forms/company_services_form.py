from company_services.helpers import PasswordHasher
from company_services.models import CompanyService
from core.forms import BaseModelFormMixin
from django import forms

from core.utils import debugging_print


class CompanyServiceForm(BaseModelFormMixin):
    def __init__(self, client=None, is_update=False, updated_object=None, *args, **kwargs):
        super(CompanyServiceForm, self).__init__(*args, **kwargs)
        # debugging_print(self.fields)
        self.is_update = is_update
        self.updated_object = updated_object
        if client is not None:
            self.fields["client"].initial = client
        # if self.is_update is True:
        #     # pass
        #     self.initial["password"] = self.updated_object.decrypted_password

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}), required=False
    )

    def clean_password(self):
        data = self.cleaned_data["password"]
        if self.is_update is True:
            debugging_print("Update")
            if not data:
                debugging_print("No password")
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
        # widgets = {"password": forms.PasswordInput(attrs={"autocomplete": "new-password"})}
