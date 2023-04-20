# -*- encoding: utf-8 -*-
from core.utils import debugging_print
from decouple import config
from bookkeeper.tests.factories.bookkeeper_factory import BookkeeperProxyFactory
from factory import Faker
from django.db import transaction


from core.utils.developments.debugging_print import debugging_colored_print
from users.tests.factories.users_factory import UserFactory


def run(*args):
    # print(Fore.YELLOW + f"Start flush (Discussion) table:")
    debugging_print(args)
    environment = config("STAGE_ENVIRONMENT", cast=str)
    debugging_colored_print(f"Current environment: {environment}", "cyan", mark="****")
    if environment == "TEST":
        with transaction.atomic():
            # debugging_print(d)
            # bookkeeper = BookkeeperProxyFactory()
            # debugging_print(bookkeeper)
            new_users = UserFactory.create_batch(10)
            for user in new_users:
                debugging_print(user)
                debugging_print(user.bookkeeper)
            for user in new_users:
                debugging_colored_print(f"Delete user {user}", "yellow", mark="*")

                # debugging_print(user.bookkeeper)
                user.delete()
    else:
        debugging_colored_print(
            f"The environment not TEST! - current ({environment})", "red"
        )
