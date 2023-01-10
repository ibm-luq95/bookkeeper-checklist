from .dashboard import DashboardHomeView
from .users import UserCreateView, UserDetailsView
from .bookkeeper import (
    BookkeepersListView,
    BookkeepersDetailsView,
    BookkeeperDeleteView,
    BookkeeperCreateView,
    BookkeeperUpdateView,
    BookkeepersArchiveView,
)
from .client import (
    ClientListView,
    ClientCreateView,
    ClientDetailView,
    ClientUpdateView,
    ClientDeleteView,
    ClientArchiveListView,
)
from .jobs import (
    JobListView,
    JobCreateView,
    JobDetailsView,
    JobUpdateView,
    JobDeleteView,
    JobArchiveListView,
)
from .client_account import (
    ClientAccountCreateView,
    ClientAccountListView,
    ClientAccountDetailView,
)
from .task import (
    TasksListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TasksArchiveListView,
)
from .company_service import (
    CompanyServicesListView,
    CompanyServicesDeleteView,
    CompanyServicesCreateView,
    CompanyServicesUpdateView,
)
from .assistant import (
    AssistantListView,
    AssistantDetailsView,
    AssistantDeleteView,
    AssistantUpdateView,
    AssistantCreateView,
)
from .special_assignment import (
    SpecialAssignmentListView,
    SpecialAssignmentCreateView,
    SpecialAssignmentUpdateView,
    SpecialAssignmentDeleteView,
    SpecialAssignmentDetailsView,
)
