from core.forms import BaseModelFormMixin
from client_account.models import ClientAccount
from django import forms


class ClientAccountForm(BaseModelFormMixin):
    def __init__(self, client=None, *args, **kwargs):
        super(ClientAccountForm, self).__init__(*args, **kwargs)
        # if client is not None:
            # print(self.fields.get("client"))
            # self.fields["client"].initial = client
        self.fields["account_url"].widget.attrs.update({"class": "input", "type": "url"})

    class Meta(BaseModelFormMixin.Meta):
        model = ClientAccount
        exclude = ["metadata", "is_deleted", "deleted_at"]
        # widgets = {
        #     "account_url": forms.URLInput()
        # }
