from rest_framework import serializers

from respondents.models import Respondent


class RespondentSerializer(serializers.ModelSerializer):
    '''Сериалтзатор респондента'''
    class Meta:
        model = Respondent
        fields = ('first_name',
                  'last_name',
                  'chat_tg_id',
                  )
