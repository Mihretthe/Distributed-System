from django.contrib import admin
from .models import UserActivity, HealthMetrics

admin.site.register(UserActivity)
admin.site.register(HealthMetrics)

