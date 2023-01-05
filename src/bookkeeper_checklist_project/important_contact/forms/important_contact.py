# -*- coding: utf-8 -*-#
from client.models import Client
from core.forms import BaseModelFormMixin, Html5Mixin
from important_contact.models import ImportantContact


class ImportantContactForm(BaseModelFormMixin, Html5Mixin):
    # auto_id = "important_contact_%s"

    def __init__(
        self,
        is_readonly=False,
        client_pk=None,
        is_creating=False,
        remove_client_field=False,
        *args,
        **kwargs
    ):
        super(ImportantContactForm, self).__init__(*args, **kwargs)
        # print(is_creating)

        if is_readonly is True:
            for field in self.fields:
                self.fields[field].widget.attrs.update({"readonly": "readonly"})
            self.fields["contact_label"].widget.attrs.update({"class": "readonly-select"})

        # check if the client passed in the arguments
        if client_pk is not None:
            self.fields["client"].initial = (
                Client.objects.select_related().filter(pk=client_pk).first()
            )

        # remove client input
        if remove_client_field is True:
            self.fields.pop("client")

    class Meta(BaseModelFormMixin.Meta):
        model = ImportantContact
        # widgets = {
        #     "account_url": forms.URLInput()
        # }
