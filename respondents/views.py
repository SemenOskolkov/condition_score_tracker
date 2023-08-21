from django.views.generic import TemplateView
from rest_framework import generics
from respondents.models import Respondent
from respondents.serializers import RespondentSerializer


class RespondentListView(generics.ListAPIView):
    """Контроллер для работы с клиентами"""
    serializer_class = RespondentSerializer
    queryset = Respondent.objects.all()


class LinkTelegramBotView(TemplateView):
    """Страница со ссылкой на телеграмм бот"""
    template_name = 'respondents/link_for_client.html'
