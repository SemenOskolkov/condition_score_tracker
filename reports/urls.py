from rest_framework.routers import DefaultRouter

from reports.apps import ReportsConfig
from reports.views import ReportViewSet

app_name = ReportsConfig.name

router = DefaultRouter()
router.register(r'reports', ReportViewSet, basename='reports')

urlpatterns = []

urlpatterns += router.urls
