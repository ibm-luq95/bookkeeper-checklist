from .dashboard import DashboardView
from .bookkeepers import BookkeepersListView, BookkeepersDetailsView
from .client import (
    ClientListView,
    ClientCreateView,
    ClientDetailsView,
    ClientUpdateView,
    ClientDetailsJobsView,
    ClientDetailsTasksView,
    ClientDetailsSpecialAssignmentsView,
    ClientDetailsDocumentsView,
    ClientDetailsNotesView,
    ClientDetailsAccountsAndServicesView,
    ClientDetailsOverviewRedirectView,
    ClientDetailsContactsView,
)
from .important_contact import ImportantContactListView, ImportantContactCreateView
from .job import JobListView, JobCreateView
