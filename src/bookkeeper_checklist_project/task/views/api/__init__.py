# -*- coding: utf-8 -*-#
from .manager import (
    CreateTaskManagerApiView,
    RetrieveTaskManagerApiView,
    UpdateTaskManagerApiView,
    DeleteTaskManagerApiView,
)
from .bookkeeper import SetTaskCompletedBookkeeperApiView, TaskBookkeeperRetrieveAPIView
