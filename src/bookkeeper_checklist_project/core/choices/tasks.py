# -*- coding: utf-8 -*-#
import stringcase
from django.db import models
from django.utils.translation import gettext as _

from core.constants.status_labels import (
    CON_ARCHIVED,
    CON_COMPLETED,
    CON_IN_PROGRESS,
    CON_NOT_STARTED,
)
from core.constants.types_labels import (
    CON_NO_TYPE,
    CON_RECURRING,
    CON_WEEKLY,
    CON_MONTHLY,
    CON_QUARTERLY,
    CON_YEARLY,
    CON_ONE_TIME,
    CON_URGENT,
)


class TaskStatusEnum(models.TextChoices):
    NOT_STARTED = CON_NOT_STARTED, _(stringcase.sentencecase(CON_NOT_STARTED))
    IN_PROGRESS = CON_IN_PROGRESS, _(stringcase.sentencecase(CON_IN_PROGRESS))
    COMPLETED = CON_COMPLETED, _(stringcase.sentencecase(CON_COMPLETED))
    ARCHIVED = CON_ARCHIVED, _(stringcase.sentencecase(CON_ARCHIVED))


class TaskTypeEnum(models.TextChoices):
    NO_TYPE = CON_NO_TYPE, _(stringcase.sentencecase(CON_NO_TYPE))
    RECURRING = CON_RECURRING, _(stringcase.sentencecase(CON_NO_TYPE))
    WEEKLY = CON_WEEKLY, _(stringcase.sentencecase(CON_WEEKLY))
    MONTHLY = CON_MONTHLY, _(stringcase.sentencecase(CON_MONTHLY))
    QUARTERLY = CON_QUARTERLY, _(stringcase.sentencecase(CON_QUARTERLY))
    YEARLY = CON_YEARLY, _(stringcase.sentencecase(CON_YEARLY))
    ONE_TIME = CON_ONE_TIME, _(stringcase.sentencecase(CON_ONE_TIME))
    URGENT = CON_URGENT, _(stringcase.sentencecase(CON_URGENT))
