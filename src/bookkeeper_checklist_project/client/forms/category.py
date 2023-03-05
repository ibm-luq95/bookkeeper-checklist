# -*- coding: utf-8 -*-#
from core.forms import BaseModelFormMixin
from client.models import ClientCategory


class ClientCategoryForm(BaseModelFormMixin):
    def __init__(self, *args, **kwargs):
        super(ClientCategoryForm, self).__init__(*args, **kwargs)

    class Meta(BaseModelFormMixin.Meta):
        model = ClientCategory
