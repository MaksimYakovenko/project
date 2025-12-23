from rest_framework import permissions


class IsAdminUserOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Дозволяємо GET, HEAD, OPTIONS для всіх
        if request.method in permissions.SAFE_METHODS:
            return True

        # Для POST, PUT, PATCH, DELETE перевіряємо чи це admin
        return request.user and request.user.is_authenticated and request.user.username == 'admin'

    def has_object_permission(self, request, view, obj):
        # Дозволяємо читання для всіх
        if request.method in permissions.SAFE_METHODS:
            return True

        # Редагування та видалення тільки для admin
        return request.user and request.user.is_authenticated and request.user.username == 'admin'

