from rest_framework import serializers
from .models import UserActivity, HealthMetrics

class UserActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserActivity
        fields = '__all__'
    """
    # adding this onec the user management is one to check the user is authenticated
    def validate_user_id(self, value):
        response = requests.get(f'http://user-management-service/api/users/{value}')
        if response.status_code != 200:
            raise ValidationError("User ID is not valid.")
        return value
    """
class HealthMetricsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthMetrics
        fields = '__all__'
