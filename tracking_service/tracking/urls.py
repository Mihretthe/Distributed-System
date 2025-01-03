from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import UserActivityViewSet, HealthMetricsViewSet, CustomTokenRefreshView

router = DefaultRouter()
router.register(r'user-activities', UserActivityViewSet, basename='useractivity')
router.register(r'health-metrics', HealthMetricsViewSet, basename='healthmetrics')

urlpatterns = [
    path('', include(router.urls)),
    path('api/token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
]
