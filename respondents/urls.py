from django.urls import path
from respondents.apps import RespondentsConfig

from respondents.views import *


app_name = RespondentsConfig.name


urlpatterns = [
    path('respondents/', RespondentListView.as_view(), name='respondents_list'),
    path('link_bot/', LinkTelegramBotView.as_view(), name='link_telegram_bot'),
]
