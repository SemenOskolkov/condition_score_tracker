from rest_framework import serializers

from reports.models import Report


class ReportSerializer(serializers.ModelSerializer):
    '''Сериализатор отчетов клиентов'''
    class Meta:
        model = Report
        fields = '__all__'


class ReportListSerializer(serializers.ModelSerializer):
    '''Сериализатор страницы отчетов клиентов'''
    class Meta:
        model = Report
        fields = (
            'respondent',
            'creat_at',
        )
        