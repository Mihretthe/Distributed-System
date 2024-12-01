from django.db import models

class Child(models.Model):
    name = models.CharField(max_length=50)
    parent = models.ForeignKey('user_management.User', on_delete=models.CASCADE)
    age = models.IntegerField()
    special_needs = models.TextField(blank=True)


class Location(models.Model):
    child = models.ForeignKey(Child, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
