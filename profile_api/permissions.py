from rest_framework.permissions import BasePermission


class UpdateOwnProfile(BasePermission):
    """Allow user to edit their own profile"""
    message = "You must be owner of this object to edit"

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""
        # if request.method in permissions.SAFE_METHODS:
        #     return True
        return obj.id == request.user.id
