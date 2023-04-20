import os
import traceback

from django.contrib.auth.models import Group, Permission
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver

from assistant.models import Assistant
from bookkeeper.models import BookkeeperProxy
from core.cache import BWCacheHandler
from core.constants import BOOKKEEPER_GROUP_NAME, MANAGER_GROUP_NAME, ASSISTANT_GROUP_NAME
from core.constants.site_settings import WEB_APP_SETTINGS_KEY, APP_CONFIGS_SETTINGS_KEY
from core.utils import ProjectError
from core.utils import get_formatted_logger
from manager.models import Manager
from site_settings.models import SiteSettings, ApplicationConfigurations
from users.models import CustomUser

# TODO: remove the custom logger before push (only for development)
# ###### [Custom Logger] #########
logger = get_formatted_logger()


# ###### [Custom Logger] #########


@receiver(post_save, sender=CustomUser)
def create_groups(sender, instance, created, **kwargs):
    try:
        # raise Exception("D")
        if created is True:
            with transaction.atomic():
                # print("create group")
                group = None
                permission_codename = None
                user = instance
                user_type = user.user_type

                match user_type:
                    case "bookkeeper":
                        group = BOOKKEEPER_GROUP_NAME
                        permission_codename = "bookkeeper_user"
                        bookkeeper = BookkeeperProxy.objects.create(user=user)

                    case "assistant":
                        group = ASSISTANT_GROUP_NAME
                        permission_codename = "assistant_user"
                        assistant = Assistant.objects.create(user=user)
                    case "manager":
                        group = MANAGER_GROUP_NAME
                        permission_codename = "manager_user"
                        manager = Manager.objects.create(user=user)
                    case _:
                        if user.is_staff is True and user.is_superuser is True:
                            group = MANAGER_GROUP_NAME
                            user.user_type = "manager"
                            user.save()
                group_object = Group.objects.filter(name=group)

                if not group_object:
                    raise ProjectError("USER", message=f"The group {group} not exists!")
                group_object = group_object.first()
                # print(group_object)
                user.user_permissions.add(
                    Permission.objects.get(codename=permission_codename)
                )
                user.groups.add(group_object)
                user.save()
        else:
            # check if the user is deleted, this will use here instead of using post_delete signal
            # because I used soft delete functionality
            if (
                instance.is_deleted is True
                and instance.get_changed_columns().get("is_deleted") is False
            ):
                user_type = instance.user_type
                if user_type == "bookkeeper":
                    check_if_bookkeeper = hasattr(instance, "bookkeeper")
                    if check_if_bookkeeper is True:
                        bookkeeper_obj = instance.bookkeeper
                        bookkeeper_proxy_obj = BookkeeperProxy.objects.get(
                            pk=bookkeeper_obj.pk
                        )
                        if hasattr(bookkeeper_proxy_obj, "clients"):
                            clients = bookkeeper_proxy_obj.clients.all()
                            if clients:
                                for client in clients:
                                    # check if the bookkeeper exists in the client bookkeepers,
                                    # this step just in case
                                    contains = client.bookkeepers.contains(
                                        bookkeeper_proxy_obj
                                    )
                                    if contains is True:
                                        client.bookkeepers.remove(bookkeeper_proxy_obj)
                                        client.save()
                        bookkeeper_obj.delete()
                if user_type == "assistant":
                    assistant_obj = instance.assistant
                    assistant_obj.delete()
                if user_type == "manager":
                    manager_obj = instance.manager
                    manager_obj.delete()

    except Exception as ex:
        logger.error(traceback.format_exc())
        raise Exception(str(ex))


@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    # if user.user_type == "manager":
    site_settings = SiteSettings.objects.select_related().filter(slug="web-app").first()
    app_configs = ApplicationConfigurations.objects.filter(slug="app-configs").first()
    if site_settings:
        BWCacheHandler.set_item(WEB_APP_SETTINGS_KEY, site_settings)
    if app_configs:
        BWCacheHandler.set_item(APP_CONFIGS_SETTINGS_KEY, app_configs)


# @receiver(user_logged_out)
# def log_user_logout(sender, request, user, **kwargs):
#     stage = os.environ.get("STAGE_ENVIRONMENT")
#     if stage == "DEV" and user.user_type == "manager":
#         BWCacheHandler.clear()


# post_delete.connect(delete_user_vacuum, sender=get_user_model())
