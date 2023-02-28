from .dashboard import DashboardHomeView
from .users import UserCreateView, UserDetailsView, UserUpdateView
from .bookkeeper import (
    BookkeepersListView,
    BookkeepersDetailsView,
    BookkeeperDeleteView,
    BookkeeperCreateView,
    BookkeeperUpdateView,
    BookkeepersArchiveView,
)
from .assistant import (
    AssistantListView,
    AssistantDetailsView,
    AssistantDeleteView,
    AssistantUpdateView,
    AssistantCreateView,
)

from .manager import (
    ManagerListView,
    ManagerCreateView,
    ManagerDeleteView,
    ManagerArchiveView,
    ManagerUpdateView,
    ManagerDetailsView,
)
