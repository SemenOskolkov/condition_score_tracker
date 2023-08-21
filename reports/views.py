from rest_framework import viewsets

from reports.models import Report
from reports.serializers import ReportSerializer, ReportListSerializer
from users.permissions import UserPermission


class ReportViewSet(viewsets.ModelViewSet):
    '''Контроллер для работы с отчетами'''
    queryset = Report.objects.all()
    default_serializer = ReportSerializer
    serializers = {
        'list': ReportListSerializer,
        'retrieve': ReportSerializer,
    }
    permission_classes = [UserPermission]
