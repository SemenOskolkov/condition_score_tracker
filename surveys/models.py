from django.db import models


class Survey(models.Model):
    '''Модель опросов клиентов'''
    GRADE = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )

    respondent = models.ForeignKey('respondents.Respondent', on_delete=models.CASCADE, verbose_name='Респондент')
    mood = models.PositiveIntegerField(choices=GRADE, verbose_name='Настроение')
    energy = models.PositiveIntegerField(choices=GRADE, verbose_name='Энергия')
    poll_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата опроса')

    class Meta:
        verbose_name = 'опрос'
        verbose_name_plural = 'опросы'

    def __str__(self):
        return f'{self.respondent} {self.mood} {self.energy}'
