from rest_framework import PermissionsMixin


class updateOwnProfile(permissions.BasePermissions):
    """Allow users to edit ther own profile."""

    def has_objects_permissions(self, request, view, obj):
        """Check user is trying to edit ther own profile."""

    if request.method in permissions.SAFE_METHODS:
        return True

    return obj.id == request.user.id   
