from client.models import Client
from core.models import StaffModelMixin
from django.db import models
from django.utils.translation import gettext as _


class Bookkeeper(StaffModelMixin):
    clients = models.ManyToManyField(to=Client)
