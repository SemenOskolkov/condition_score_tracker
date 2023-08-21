from rest_framework.permissions import BasePermission


class UserPermission(BasePermission):
    '''Права доступа на просмотр, изменение, удаление, создание для пользователей'''
    def has_permission(self, request, view):
        if not request.user.is_authenticated and request.user.is_active:
            return False

        if view.action == 'list':
            return request.user.is_staff
        elif view.action in ['create', 'update', 'partial_update']:
            return request.user.is_supervisor or request.user.is_superuser
        elif view.action in ['retrieve']:
            return True
        elif view.action == 'destroy':
            return request.user.is_superuser
        else:
            return False

    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated and request.user.is_active:
            return False

        if view.action == 'retrieve':
            return obj == request.user or request.user.is_supervisor or request.user.is_superuser
        else:
            return False
