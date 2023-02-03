from rest_framework.permissions import BasePermission


class IsUserOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(request.user.id == obj.id)


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(request.user.id == obj.owner.id)


