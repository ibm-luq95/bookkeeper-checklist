# -*- coding: utf-8 -*-#
from client.models import Client
from core.utils import debugging_print


def run(*args):
    clients = Client.objects.all()
    for client in clients:
        debugging_print(client)
        debugging_print("####################################")
        bookkeepers = client.bookkeepers.all()
        if bookkeepers:
            for bookkeeper in bookkeepers:
                debugging_print(bookkeeper.get_bookkeeper)
        # b = bookkeepers.first()
        # if b:
            # debugging_print(b._meta.get_fields(include_parents=True, include_hidden=True))
