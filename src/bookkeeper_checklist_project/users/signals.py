import traceback
import os
from django.contrib.auth.models import Group
from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed

from core.constants import BOOKKEEPER_GROUP_NAME, MANAGER_GROUP_NAME, ASSISTANT_GROUP_NAME
from core.utils import ProjectError, debugging_print
from core.utils import get_formatted_logger
from users.models import CustomUser
from core.cache import CacheHandler
from site_settings.models import SiteSettings
from core.constants.site_settings import WEB_APP_SETTINGS_KEY

# TODO: remove the custom logger before push (only for development)
# ###### [Custom Logger] #########
logger = get_formatted_logger(__name__)


# ###### [Custom Logger] #########


@receiver(post_save, sender=CustomUser)
def create_groups(sender, instance, created, **kwargs):
    try:
        if created:
            with transaction.atomic():

                # print("create group")
                group = None
                user = instance
                user_type = user.user_type

                match user_type:
                    case "bookkeeper":
                        group = BOOKKEEPER_GROUP_NAME
                    case "assistant":
                        group = ASSISTANT_GROUP_NAME
                    case "manager":
                        group = MANAGER_GROUP_NAME
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
                instance.groups.add(group_object)
                instance.save()
    except ProjectError as ex:
        logger.error(ex.message)
        logger.error(traceback.format_exc())

    except Exception as ex:
        logger.error(traceback.format_exc())
        raise Exception(str(ex))


@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    # if user.user_type == "manager":
    site_settings = SiteSettings.objects.select_related().filter(slug="web-app").first()
    if site_settings:
        CacheHandler.set_item(WEB_APP_SETTINGS_KEY, site_settings)


@receiver(user_logged_out)
def log_user_logout(sender, request, user, **kwargs):
    stage = os.environ.get("STAGE_ENVIRONMENT")
    if stage == "DEV" and user.user_type == "manager":
        CacheHandler.clear()
