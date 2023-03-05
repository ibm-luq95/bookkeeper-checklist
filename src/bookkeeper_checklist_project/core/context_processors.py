# -*- coding: utf-8 -*-#
from core.constants.status_labels import (
    CON_ENABLED,
    CON_COMPLETED,
    CON_ARCHIVED,
    CON_IN_PROGRESS,
    CON_DISABLED,
    CON_REJECTED,
    CON_NOT_STARTED,
    CON_NOT_COMPLETED,
    CON_PAST_DUE,
    CON_DRAFT,
    CON_PENDING,
    CON_CANCELED,
)


def access_constants(request) -> dict:
    """
    The context processor will return project constants as dict
    """
    return {
        "CON_ENABLED": CON_ENABLED,
        "CON_IN_PROGRESS": CON_IN_PROGRESS,
        "CON_ARCHIVED": CON_ARCHIVED,
        "CON_COMPLETED": CON_COMPLETED,
        "CON_DISABLED": CON_DISABLED,
        "CON_REJECTED": CON_REJECTED,
        "CON_NOT_STARTED": CON_NOT_STARTED,
        "CON_NOT_COMPLETED": CON_NOT_COMPLETED,
        "CON_PAST_DUE": CON_PAST_DUE,
        "CON_PENDING": CON_PENDING,
        "CON_CANCELED": CON_CANCELED,
        "CON_DRAFT": CON_DRAFT,
    }
