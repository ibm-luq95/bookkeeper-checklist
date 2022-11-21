from .dashboard import DashboardHomeView
from .users import UserCreateView, UserDetailsView
from .bookkeeper import (
    BookkeepersListView,
    BookkeepersDetailsView,
    BookkeeperDeleteView,
)
from .client import (
    ClientListView,
    ClientCreateView,
    ClientDetailView,
    ClientUpdateView,
    ClientDeleteView,
)
from .jobs import JobListView, JobCreateView, JobDetailsView
from .client_account import (
    ClientAccountCreateView,
    ClientAccountListView,
    ClientAccountDetailView,
)
