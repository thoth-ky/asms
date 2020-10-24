from django.urls import path

from accounts.views import OrganizationListCreateView
from accounts.views import UserDetail
from accounts.views import UsersCreateView
from accounts.views import UsersListView


urlpatterns = [
    path(
        "organizations/", OrganizationListCreateView.as_view(), name="org_list_create"
    ),
    path("users/", UsersListView.as_view(), name="user_list"),
    path("users/create", UsersCreateView.as_view(), name="user_create"),
    path("users/<str:username>", UserDetail.as_view(), name="user_detail"),
]
