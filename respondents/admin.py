from django.contrib import admin

from respondents.models import Respondent


@admin.register(Respondent)
class RespondentAdmin(admin.ModelAdmin):
    list_display = ('respondent_tg_id', 'first_name', 'last_name', 'chat_tg_id', 'last_report_sent',)
