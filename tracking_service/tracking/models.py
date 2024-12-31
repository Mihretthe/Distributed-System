from django.db import models

class UserActivity(models.Model):
    user_id = models.UUIDField()  # ForeignKey-like relationship to User Management service
    date = models.DateField()
    steps = models.IntegerField(default=0)
    distance_km = models.FloatField(default=0.0)
    calories_burned = models.FloatField(default=0.0)

class HealthMetrics(models.Model):
    user_id = models.UUIDField()  # ForeignKey-like relationship to User Management service
    date = models.DateField()
    heart_rate = models.IntegerField(null=True, blank=True)  # bpm
    sleep_hours = models.FloatField(null=True, blank=True)
    water_intake_liters = models.FloatField(null=True, blank=True)
    weight_kg = models.FloatField(null=True, blank=True)
