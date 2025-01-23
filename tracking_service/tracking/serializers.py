from rest_framework import serializers
from .models import UserActivity, HealthMetrics
import requests
from rest_framework.serializers import ValidationError
class UserActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserActivity
        fields = '__all__'
    """
    # adding this once the user management is one to check the user is authenticated
    def validate_user_id(self, value):
        response = requests.get(f'http://user-management-service/api/users/{value}')
        if response.status_code != 200:
            raise ValidationError("User ID is not valid.")
        return value
    """
    def validate_user_id(self, value):
        """
        Validate the user_id by checking with the User Management Service.
        """
        try:
            user_service_url = f'http://127.0.0.1:8001/user/user/{value}'  # Use 127.0.0.1 for testing
            response = requests.get(user_service_url, timeout=5)
            print(f"Response: {response.status_code} - {response.text}")  # Log the response details
            if response.status_code != 200:
                print("20000")
                raise ValidationError(f"User ID {value} is not valid. User Management Service responded with {response.status_code}.")
        except requests.exceptions.RequestException as e:
            print("meeee")
            raise ValidationError(f"Error connecting to User Management Service: {e}")
        except:
            print("I donno")
        
        return value

class HealthMetricsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthMetrics
        fields = '__all__'
    
    def validate_user_id(self, value):
        """
        Validate the user_id by checking with the User Management Service.
        """
        try:
            user_service_url = f'http://127.0.0.1:8001/user/user/{value}'  # Use 127.0.0.1 for testing
            response = requests.get(user_service_url, timeout=5)
            print(f"Response: {response.status_code} - {response.text}")  # Log the response details
            if response.status_code != 200:
                print("20000")
                raise ValidationError(f"User ID {value} is not valid. User Management Service responded with {response.status_code}.")
        except requests.exceptions.RequestException as e:
            print("meeee")
            raise ValidationError(f"Error connecting to User Management Service: {e}")
        except:
            print("I donno")
        
        return value
