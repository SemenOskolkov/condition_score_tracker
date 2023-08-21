from datetime import datetime

from celery import shared_task

from respondents.models import Respondent
from respondents.management.commands.telegram_bot import ask_mood
from config import settings


@shared_task
def send_daily_survey():
    '''Отправка ежедневного опроса через бот в 17:00'''
    time_now = datetime.now().time()
    if time_now.hour == settings.SEND_SURVEY_HOUR and time_now.minute == settings.SEND_SURVEY_MINUTE:
        respondents = Respondent.objects.all()  # Получаем список всех клиентов
        for respondent in respondents:
            ask_mood(respondent.respondent_tg_id)  # Отправляем опрос текущему клиенту
