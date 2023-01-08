from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext as _
from django.db import transaction

from core.models import BaseQuerySetMixin
from core.utils import debugging_print



class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def get_queryset(self) -> BaseQuerySetMixin:
        queryset = BaseQuerySetMixin(self.model, using=self._db).filter(is_deleted=False)
        return queryset

    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        with transaction.atomic():
            if not email:
                raise ValueError(_("The Email must be set"))
            email = self.normalize_email(email)
            user = self.model(email=email, **extra_fields)
            user.set_password(password)
            user.save()
            # if user.user_type == "manager":
            #     Manager.objects.select_for_update().create(user=user)
            return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        with transaction.atomic():
            from manager.models import Manager
            extra_fields.setdefault("is_staff", True)
            extra_fields.setdefault("is_superuser", True)
            extra_fields.setdefault("is_active", True)

            # create admin names for superuser in case it is admin
            if email == "admin@admin.com":
                extra_fields.setdefault("first_name", "Administrator")
                extra_fields.setdefault("last_name", "Account")
                extra_fields.setdefault("user_type", "manager")

            if extra_fields.get("is_staff") is not True:
                raise ValueError(_("Superuser must have is_staff=True."))
            if extra_fields.get("is_superuser") is not True:
                raise ValueError(_("Superuser must have is_superuser=True."))
            created_user = self.create_user(email, password, **extra_fields)
            # debugging_print("##############")
            if created_user.user_type == "manager":
                manager = Manager.objects.select_related().create(user=created_user)
                # debugging_print(created_user)
                # debugging_print(manager)
            # debugging_print("##############")
            return created_user
