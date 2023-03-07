# -*- coding: utf-8 -*-#
from django.db import transaction
from django.db.models.signals import post_save

from client.models import ClientProxy
from core.utils import debugging_print


def archive_all_related_items_for_client(
    sender, instance: ClientProxy, created: bool, **kwargs
):
    if not created:
        with transaction.atomic():
            client_object = instance
            # debugging_print(client_object.get_changed_columns())
            # debugging_print(client_object)
            client_object.archive_all_items()


post_save.connect(archive_all_related_items_for_client, ClientProxy)
