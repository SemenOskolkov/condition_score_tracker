from config import settings
import requests

import statistics
from datetime import datetime, timedelta

from surveys.models import Survey
from reports.models import Report


def calculate_moda_mood(respondent):
    '''Расчет моды настроения клиента за последние 7 дней'''
    last_week = datetime.now() - timedelta(days=7)
    mood_values = Survey.objects.filter(respondent=respondent, poll_date__gte=last_week).values_list('mood', flat=True)
    if mood_values:
        moda_mood = statistics.mode(mood_values)
    else:
        moda_mood = None
    return moda_mood


def calculate_moda_energy(respondent):
    '''Расчет моды энергии клиента за последние 7 дней'''
    last_week = datetime.now() - timedelta(days=7)
    energy_values = Survey.objects.filter(respondent=respondent, poll_date__gte=last_week).values_list('energy', flat=True)
    if energy_values:
        moda_energy = statistics.mode(energy_values)
    else:
        moda_energy = None
    return moda_energy


def calculate_average_mood(respondent):
    '''Расчет средней оценки настроения клиента за последние 7 дней'''
    last_week = datetime.now() - timedelta(days=7)
    mood_values = Survey.objects.filter(respondent=respondent, poll_date__gte=last_week).values_list('mood', flat=True)
    if mood_values:
        average_mood = statistics.mean(mood_values)
    else:
        average_mood = None
    return average_mood


def calculate_average_energy(respondent):
    '''Расчет средней оценки энергии клиента за последние 7 дней'''
    last_week = datetime.now() - timedelta(days=7)
    energy_values = Survey.objects.filter(respondent=respondent, poll_date__gte=last_week).values_list('energy', flat=True)
    if energy_values:
        average_energy = statistics.mean(energy_values)
    else:
        average_energy = None
    return average_energy


def generate_report(respondent):
    '''Сохранение вычислений в базе данных'''
    survey_entries = Survey.objects.filter(
        respondent=respondent)  # Проверка, на наличие записи опросов для формирования отчета

    if not survey_entries:
        print("Нет записей опросов для формирования отчета")
        return

    moda_mood = calculate_moda_mood(respondent)
    moda_energy = calculate_moda_energy(respondent)
    average_mood = calculate_average_mood(respondent)
    average_energy = calculate_average_energy(respondent)

    mood_report = Report(respondent=respondent, moda_mood=moda_mood, moda_energy=moda_energy, average_mood=average_mood,
                         average_energy=average_energy)

    report_text = f"Отчет за последние 7 дней.\n"
    report_text += f"Чаще всего вы чувствовали себя:\n-Настроение - {moda_mood}\n-Энергия - {moda_energy}\n"
    report_text += f"Средняя оценка за неделю:\n-Настроение - {average_mood}\n-Энергия - {average_energy}"

    mood_report.save()

    send_report_to_telegram(respondent.chat_tg_id, report_text)


def send_report_to_telegram(telegram_chat_id, report_text):
    '''Отправка отчета пользователю в Telegram'''

    data_for_request = {
        "chat_id": telegram_chat_id,
        "text": report_text
    }
    response = requests.post(f'{settings.TELEGRAM_URL}{settings.TELEGRAM_BOT_TOKEN}/sendMessage', data_for_request)
    if response.status_code != 200:
        print(f"Ошибка при отправке отчета в Telegram")
