from rest_framework import viewsets
from drf_spectacular.utils import extend_schema_view, extend_schema
import rest_framework
from .models import UserActivity, HealthMetrics
from .serializers import UserActivitySerializer, HealthMetricsSerializer
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.views import TokenRefreshView

class CustomTokenRefreshView(TokenRefreshView):
    renderer_classes = [rest_framework.renderers.JSONRenderer]


@extend_schema_view(
    list=extend_schema(tags=["User Activities"]),
    retrieve=extend_schema(tags=["User Activities"]),
    create=extend_schema(tags=["User Activities"]),
    update=extend_schema(tags=["User Activities"]),
    partial_update=extend_schema(tags=["User Activities"]),
    destroy=extend_schema(tags=["User Activities"]),
)
class UserActivityViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user activity instances.
    """
    queryset = UserActivity.objects.all()
    serializer_class = UserActivitySerializer
    permission_classes = [IsAuthenticated]

@extend_schema_view(
    list=extend_schema(tags=["Health Metrics"]),
    retrieve=extend_schema(tags=["Health Metrics"]),
    create=extend_schema(tags=["Health Metrics"]),
    update=extend_schema(tags=["Health Metrics"]),
    partial_update=extend_schema(tags=["Health Metrics"]),
    destroy=extend_schema(tags=["Health Metrics"]),
)
class HealthMetricsViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing health metrics instances.
    """
    queryset = HealthMetrics.objects.all()
    serializer_class = HealthMetricsSerializer
    permission_classes = [IsAuthenticated]
