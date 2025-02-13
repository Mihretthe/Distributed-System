# Generated by Django 5.1.4 on 2024-12-31 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HealthMetrics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.UUIDField()),
                ('date', models.DateField()),
                ('heart_rate', models.IntegerField(blank=True, null=True)),
                ('sleep_hours', models.FloatField(blank=True, null=True)),
                ('water_intake_liters', models.FloatField(blank=True, null=True)),
                ('weight_kg', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.UUIDField()),
                ('date', models.DateField()),
                ('steps', models.IntegerField(default=0)),
                ('distance_km', models.FloatField(default=0.0)),
                ('calories_burned', models.FloatField(default=0.0)),
            ],
        ),
    ]
