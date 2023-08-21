from django.contrib import admin

from surveys.models import Survey


@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    list_display = ('respondent', 'mood', 'energy', 'poll_date',)
    list_filter = ('poll_date', 'respondent',)
