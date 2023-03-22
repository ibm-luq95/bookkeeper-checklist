# -*- coding: utf-8 -*-#
from client.models import Client
from core.utils import debugging_print


def run(*args):
    clients = Client.objects.all()
    for client in clients:
        bookkeepers = client.bookkeepers.all()
        debugging_print(client)
        debugging_print(bookkeepers)
