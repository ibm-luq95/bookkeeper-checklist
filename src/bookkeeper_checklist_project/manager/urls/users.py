from django.urls import path
from manager.views import UserCreateView, UserDetailsView

urlpatterns = [
    path("create", UserCreateView.as_view(), name="users-create"),
    path("details/<uuid:pk>", UserDetailsView.as_view(), name="users-detail"),
]
