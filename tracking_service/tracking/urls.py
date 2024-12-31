from django.urls import path
from . import views

urlpatterns = [
    path('user-activities/', views.user_activity_list, name='user_activity_list'),
    path('user-activities/<int:pk>/', views.user_activity_detail, name='user_activity_detail'),
    path('health-metrics/', views.health_metrics_list, name='health_metrics_list'),
    path('health-metrics/<int:pk>/', views.health_metrics_detail, name='health_metrics_detail'),
]
