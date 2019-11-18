from rest_framework import permissions

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_admin or request.user.is_manager

    def has_object_permission(self, request, view, obj):
        return request.user.is_admin or request.user.is_manager