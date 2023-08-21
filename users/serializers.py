from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор пользователя"""
    class Meta:
        model = User
        fields = '__all__'


class UserListSerializer(serializers.ModelSerializer):
    """Сериализатор страницы с пользователями"""
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name'
        )


class UserDetailSerializer(serializers.ModelSerializer):
    """Сериализатор подробной информации о пользователе"""
    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'phone_number',
            'telegram_chat_id',
            'is_active',
            'is_staff',
            'is_supervisor',
        )
