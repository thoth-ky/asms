from django.shortcuts import get_object_or_404
from rest_framework.generics import CreateAPIView
from rest_framework.generics import ListAPIView
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.permissions import IsAuthenticated

from accounts.models import Organization
from accounts.models import User
from accounts.permissions import IsSuperUser
from accounts.serializers import OrganizationSerializer
from accounts.serializers import UserSerializer


class OrganizationListCreateView(ListCreateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [
        IsSuperUser,
    ]


class UsersListView(ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [
        IsAdminUser,
    ]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return User.objects.all()
        elif user.is_staff:
            return User.objects.filter(organization=user.organization)


class UsersCreateView(CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

    def perform_create(self, serializer):
        user = self.request.user
        if user.is_superuser:
            serializer.save()
        else:
            serializer.validated_data["organization"] = user.organization
            serializer.save()


class UserDetail(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def get_object(self):
        user = self.request.user
        if user.is_staff:
            return get_object_or_404(User, username=self.kwargs.get("username"))
        elif self.request.method == "GET":
            return user
