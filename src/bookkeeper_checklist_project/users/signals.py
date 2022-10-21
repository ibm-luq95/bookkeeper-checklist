import traceback

from core.utils import get_formatted_logger
from django.contrib.auth.models import Group, User
from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from core.utils import ProjectException
from users.models import CustomUser

# TODO: remove the custom logger before push (only for development)
# ###### [Custom Logger] #########
logger = get_formatted_logger(__name__)


# ###### [Custom Logger] #########


@receiver(post_save, sender=CustomUser)
def create_profile(sender, instance, created, **kwargs):
    try:
        if created:
            with transaction.atomic():

                # print("create group")
                group = None
                user = instance
                user_type = user.user_type
                match user_type:
                    case "bookkeeper":
                        group = "Bookkeeper Group"
                    case "assistant":
                        group = "Assistant Group"
                    case "manager":
                        group = "Manager Group"
                group_object = Group.objects.filter(name=group)

                if not group_object:
                    raise ProjectException(
                        "USER", message=f"The group {group} not exists!"
                    )
                group_object = group_object.first()
                # print(group_object)
                instance.groups.add(group_object)
                instance.save()

    except Exception as ex:
        logger.error(traceback.format_exc())
        raise Exception(str(ex))
