from rest_framework.permissions import BasePermission
from rest_framework.permissions import SAFE_METHODS


class IsSuperUser(BasePermission):
    message = "User does not have required permissions."

    def has_permission(self, request, view):
        return request.user.is_superuser


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS
