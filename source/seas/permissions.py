from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
  # https://www.django-rest-framework.org/tutorial/4-authentication-and-permissions/
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.contentListAuthor.id == request.user.id
