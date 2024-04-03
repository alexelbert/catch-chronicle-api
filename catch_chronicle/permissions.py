from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to limit object editing exclusively to its owner.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user

class IsNotificationOwner(permissions.BasePermission):
    """
    Granting custom permissions to limit 
    notification access only to the notification owner.
    """

    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        raise PermissionDenied(
            "403 Permission denied"
        )
