from django.contrib import admin

from reports.models import Report


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('respondent', 'moda_mood', 'moda_energy', 'average_mood', 'average_energy', 'creat_at',)
    list_filter = ('creat_at', 'respondent',)
