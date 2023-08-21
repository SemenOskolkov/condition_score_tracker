from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Respondent(models.Model):
    '''Модель респондента - пользователя телеграмм'''
    respondent_tg_id = models.BigIntegerField(unique=True, primary_key=True, verbose_name='ID респондента')
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    chat_tg_id = models.BigIntegerField(verbose_name='Чат ID телеграмма')

    last_report_sent = models.DateTimeField(**NULLABLE, verbose_name='Последняя дата отправки отчета')

    class Meta:
        verbose_name = 'респондент'
        verbose_name_plural = 'респонденты'

    def __str__(self):
        return f'{self.respondent_tg_id} {self.first_name} {self.last_name} '
