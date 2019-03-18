from rest_framework import permissions

class IsParent(permissions.BasePermission):
    """
    Custom permission to only allow parents of a baby to edit its details.
    """
    def has_object_permission(self, request, view, obj):
        # write, read permissions are only allowed to the owner of the request
        return obj.parent == request.user

