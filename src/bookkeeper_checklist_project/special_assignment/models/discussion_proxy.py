# -*- coding: utf-8 -*-#

from special_assignment.models import Discussion


class DiscussionProxy(Discussion):
    class Meta:
        proxy = True
