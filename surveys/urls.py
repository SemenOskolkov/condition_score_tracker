from rest_framework.routers import DefaultRouter

from surveys.apps import SurveysConfig
from surveys.views import SurveyViewSet

app_name = SurveysConfig.name

router = DefaultRouter()
router.register(r'survey', SurveyViewSet, basename='survey')

urlpatterns = []

urlpatterns += router.urls
