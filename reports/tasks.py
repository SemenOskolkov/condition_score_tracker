from datetime import datetime, timedelta

from celery import shared_task

from respondents.models import Respondent
from config import settings
from reports.services import generate_report


@shared_task
def send_weekly_reports():
    '''Отправка еженедельного отчета респондентам в 19:00'''
    time_now = datetime.now()  # получаем текущую дату и время
    respondents = Respondent.objects.all()  # получаем все объекты модели Respondent, чтобы выполнить отчет для каждого клиента

    for respondent in respondents:
        report_last_sent = respondent.last_report_sent  # получаем дату последней отправки отчета клиенту из поля last_report_sent модели Client
        if report_last_sent:
            time_send = report_last_sent + timedelta(
                days=settings.SEND_REPORT_PERIOD)  # расчитываем дату следующей отправки отчета, добавляя 7 дней к дате последней отправки
            if time_send == time_now.date() and time_now.hour == settings.SEND_REPORT_HOUR and time_now.minute == settings.SEND_REPORT_MINUTE:  # проверяем, наступило ли время для отправки отчета (19:00) и совпадает ли дата следующей отправки с текущей датой.
                generate_report(
                    respondent)  # вызываем функцию generate_report(), которая формирует отчет для данного клиента
                respondent.last_report_sent = time_now.date()  # обновляем поле last_report_sent модели Respondent с текущей датой, чтобы отметить, что отчет был отправлен
                respondent.save()  # сохраняем изменения модели Respondent в базе данных
        else:
            if time_now.hour == settings.SEND_REPORT_HOUR and time_now.minute == settings.SEND_REPORT_MINUTE:  # проверяем, наступило ли время для отправки отчета (19:00)
                generate_report(
                    respondent)  # вызываем функцию generate_report(), которая формирует отчет для данного клиента
                respondent.last_report_sent = time_now.date()  # обновляем поле last_report_sent модели Respondent с текущей датой, чтобы отметить, что отчет был отправлен
                respondent.save()  # сохраняем изменения модели Respondent в базе данных
