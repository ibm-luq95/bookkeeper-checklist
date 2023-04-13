# -*- encoding: utf-8 -*-
from django.db.models.signals import post_save
from factory import Faker
from factory.django import DjangoModelFactory
import factory


from users.models import CustomUser


# @factory.django.mute_signals(post_save)
class UserFactory(DjangoModelFactory):
    class Meta:
        model = CustomUser

    # bookkeeper = factory.SubFactory(
    #     "bookkeeper.factories.BookkeeperProxyFactory", bookkeeper=None
    # )
    first_name = Faker("first_name")
    last_name = Faker("last_name")
    email = Faker("email")
    # full_name = factory.LazyAttribute(lambda a: '{0} {1}'.format(a.first_name, a.last_name))
    user_type = "bookkeeper"
    password = factory.PostGenerationMethodCall("set_password", "test12356")
