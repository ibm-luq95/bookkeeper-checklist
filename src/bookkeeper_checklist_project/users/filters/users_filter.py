# -*- coding: utf-8 -*-#
import django_filters
from users.models import CustomUser


class UsersFilter(django_filters.FilterSet):
    class Meta:
        model = CustomUser
        fields = {
            "first_name": ["icontains"],
            "last_name": ["icontains"],
            "user_type": ["exact"],
            "is_active": ["exact"],
            "is_superuser": ["exact"]
        }
