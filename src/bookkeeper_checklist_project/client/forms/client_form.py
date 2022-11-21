from betterforms.multiform import MultiModelForm

from client.models import Client
from core.forms import BaseModelFormMixin
from important_contact.forms import ImportantContactForm


class ClientForm(BaseModelFormMixin):
    def __init__(self, *args, **kwargs):
        super(ClientForm, self).__init__(*args, **kwargs)
        self.fields.pop("important_contact")

    class Meta(BaseModelFormMixin.Meta):
        model = Client
        # fields = "__all__"


class ClientCreationMultiForm(MultiModelForm):
    form_classes = {
        "client": ClientForm,
        "important_contact": ImportantContactForm,
    }
