from rest_framework import serializers

from surveys.models import Survey


class SurveySerializer(serializers.ModelSerializer):
    '''Сериализатор опросов клиентов'''
    class Meta:
        model = Survey
        fields = '__all__'


class SurveyListSerializer(serializers.ModelSerializer):
    '''Сериализатор страницы опросов клиентов'''
    class Meta:
        model = Survey
        fields = (
            'user',
            'poll_date',
        )
