from users.models import CustomUser


class Manager(CustomUser):
    class Meta:
        proxy = True
        permissions = [
            ("manager_user", "Manager User"),
        ]
