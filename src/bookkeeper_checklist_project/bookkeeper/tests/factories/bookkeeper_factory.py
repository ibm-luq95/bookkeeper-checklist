# -*- encoding: utf-8 -*-
import factory
from django.db.models.signals import post_save
from factory.django import DjangoModelFactory
from factory import Faker

from bookkeeper.models import BookkeeperProxy
from users.tests.factories.users_factory import UserFactory


# @factory.django.mute_signals(post_save)
class BookkeeperProxyFactory(DjangoModelFactory):
    class Meta:
        model = BookkeeperProxy

    user = factory.RelatedFactory(UserFactory, factory_related_name="user")
