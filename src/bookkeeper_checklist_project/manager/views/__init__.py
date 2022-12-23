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
from .jobs import JobListView, JobCreateView, JobDetailsView, JobUpdateView
from .client_account import (
    ClientAccountCreateView,
    ClientAccountListView,
    ClientAccountDetailView,
)
