from django.db import models
from django.contrib.auth.models import AbstractUser, Permission, Group

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('parent', 'Parent'),
        ('therapist', 'Therapist'),
        ('admin', 'Admin')

    ]

    full_name = models.CharField(max_length=50, blank=False)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    groups = models.ManyToManyField(
        Group,
        related_name="customuser_group_set",  # Unique related_name
        blank=True,
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name="customuser_user_set",
        blank=True
    )