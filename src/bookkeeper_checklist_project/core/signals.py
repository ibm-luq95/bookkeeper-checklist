import traceback

from django.contrib.auth.models import Group
from django.db import transaction

from core.constants import BOOKKEEPER_GROUP_NAME, MANAGER_GROUP_NAME, ASSISTANT_GROUP_NAME
from core.utils import ProjectError
from core.utils import get_formatted_logger

# TODO: remove the custom logger before push (only for development)
# ###### [Custom Logger] #########
logger = get_formatted_logger()


# ###### [Custom Logger] #########


# @receiver(post_save, sender=StaffMemberMixin)
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
