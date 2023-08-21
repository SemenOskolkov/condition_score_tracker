from django.db import models


class Report(models.Model):
    '''Модель отчетов'''
    respondent = models.ForeignKey('respondents.Respondent', on_delete=models.CASCADE, verbose_name='Респондент')
    moda_mood = models.IntegerField(verbose_name='мода настроения')
    moda_energy = models.IntegerField(verbose_name='мода энергии')
    average_mood = models.FloatField(verbose_name='среднее настроения')
    average_energy = models.FloatField(verbose_name='среднее энергии')
    creat_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания отчета')

    class Meta:
        verbose_name = 'отчет'
        verbose_name_plural = 'отчеты'

    def __str__(self):
        return f'{self.respondent} {self.moda_mood} {self.moda_energy} {self.average_mood} {self.average_energy}'

