# -*- encoding: utf-8 -*-
from django.db.models.signals import post_save
from factory import Faker
from factory.django import DjangoModelFactory
import factory

from client.models import ClientProxy


class ClientFactory(DjangoModelFactory):
    class Meta:
        model = ClientProxy
