from rest_framework import viewsets

from users.models import User
from users.permissions import UserPermission
from users.serializers import UserSerializer, UserListSerializer, UserDetailSerializer


class UserViewSet(viewsets.ModelViewSet):
    """Контроллер для работы с пользователями"""
    queryset = User.objects.all()
    default_serializer = UserSerializer
    serializers = {
        'list': UserListSerializer,
        'retrieve': UserDetailSerializer,
    }
    permission_classes = [UserPermission]
