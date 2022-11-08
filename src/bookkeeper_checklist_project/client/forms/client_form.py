from core.forms import BaseModelFormMixin
from django.forms import formset_factory, inlineformset_factory
from client.forms import ClientAccountForm
from client.models import Client


class ClientForm(BaseModelFormMixin):
    class Meta(BaseModelFormMixin.Meta):
        model = Client


# ClientFormSet = inlineformset_factory(ClientForm, ClientAccountForm)
ClientFormSet = None
