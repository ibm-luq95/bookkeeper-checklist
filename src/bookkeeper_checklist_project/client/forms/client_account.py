from core.forms import BaseModelFormMixin
from client.models import ClientAccount


class ClientAccountForm(BaseModelFormMixin):
    def __init__(self, *args, **kwargs):
        super(ClientAccountForm, self).__init__(*args, **kwargs)
        self.fields["account_url"].widget.attrs.update({"class": "input"})

    class Meta(BaseModelFormMixin.Meta):
        model = ClientAccount
