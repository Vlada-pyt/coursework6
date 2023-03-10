from rest_framework.permissions import BasePermission

from users.models import UserRoles


class IsOwner(BasePermission):
    def has_permission(self, request):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, obj):
        return request.user == obj.author


class IsAdmin(BasePermission):
    def has_permission(self, request):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request):
        return request.user.role == UserRoles.ADMIN



