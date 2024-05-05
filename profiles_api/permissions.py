from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit their own profile"""
    
    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""
        # if safe method like GET, allow
        if request.method in permissions.SAFE_METHODS:
            return True

        # all other method check if allow: return True if obj id is same as person taking the actions
        return obj.id == request.user.id

