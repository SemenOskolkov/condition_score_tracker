from rest_framework import viewsets

from surveys.models import Survey
from surveys.serializers import SurveySerializer, SurveyListSerializer
from users.permissions import UserPermission


class SurveyViewSet(viewsets.ModelViewSet):
    '''Контроллер для работы с клиентами'''
    queryset = Survey.objects.all()
    default_serializer = SurveySerializer
    serializers = {
        'list': SurveyListSerializer,
        'retrieve': SurveySerializer,
    }
    permission_classes = [UserPermission]

