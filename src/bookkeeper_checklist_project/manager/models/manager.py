from users.models import CustomUser
from core.models import StaffMemberMixin, BaseModelMixin


class Manager(StaffMemberMixin):
    """Manager model represents the manager of the app

    Args:
        CustomUser (User): Django custom user model
    """

    class Meta(StaffMemberMixin.Meta):
        # proxy = True
        permissions = [
            ("manager_user", "Manager User"),
        ]
