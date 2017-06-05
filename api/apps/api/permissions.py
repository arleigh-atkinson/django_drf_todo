from rest_framework.permissions import BasePermission
from .models import Item


class IsUser(BasePermission):

    def has_object_permissions(self, request, view, obj):
        if isinstance(obj, Item):
            return obj.user == request.user
        return obj.user == request.user
