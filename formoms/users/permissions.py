from rest_framework.permissions import BasePermission

class IsAdminUser(BasePermission):
    """
    Only admin user to get a list of all users, delete users
    everyone can create a user(register)
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_staff

    def has_object_permission(self, request, view, obj):
        return request.user and request.user.is_staff


class IsOwnerOrIsAdmin(BasePermission):
    """
    Logged in user can only retrieve/update own profile
    """
    def has_object_permission(self, request, view, obj):
        return obj == request.user or request.user.is_staff