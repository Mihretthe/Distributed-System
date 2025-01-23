from rest_framework import viewsets
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from datetime import datetime
import pika
import json

from .models import UserActivity, HealthMetrics
from .serializers import UserActivitySerializer, HealthMetricsSerializer


# Function to send a message to RabbitMQ
def send_to_queue(message):
    try:
        connection = pika.BlockingConnection(
            pika.ConnectionParameters('localhost', 5672, '/', pika.PlainCredentials('guest', 'guest'))
        )
        channel = connection.channel()
        channel.queue_declare(queue='notification_queue', durable=True)

        channel.basic_publish(
            exchange='',
            routing_key='notification_queue',
            body=json.dumps(message),
            properties=pika.BasicProperties(
                delivery_mode=2,  # Make the message persistent
            ),
        )
        connection.close()
    except Exception as e:
        print(f"Error sending message to RabbitMQ: {e}")
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
    permission_classes = [AllowAny]

    @action(methods=["post"], detail=True, url_path="check-goal-and-notify")
    def check_goal_and_notify(self, request, pk=None):
        """
        Check if the user's activity count exceeds their goal count and send a notification.
        """
        try:
            # Fetch the UserActivity instance
            user_activity = UserActivity.objects.get(pk=pk)
        except UserActivity.DoesNotExist:
            raise NotFound({"error": f"UserActivity with ID {pk} does not exist."})

        # Check if the activity count exceeds the goal
        if user_activity.activity_count >= user_activity.daily_goal:
            # Prepare the success message
            message = {
                "user_id": user_activity.user_id,
                "message": "Congratulations! You have exceeded your daily goal.",
                "status": "success",
                "timestamp": datetime.now().isoformat(),
            }
            # Send notification to RabbitMQ
            send_to_queue(message)
            return Response({"status": "success", "message": "Notification sent for meeting the goal."})
        else:
            # Prepare the reminder message
            message = {
                "user_id": user_activity.user_id,
                "message": "Keep going! You haven't met your daily goal yet.",
                "status": "reminder",
                "timestamp": datetime.now().isoformat(),
            }
            # Send reminder notification to RabbitMQ
            send_to_queue(message)
            return Response({"status": "reminder", "message": "Notification sent as a reminder to meet the goal."})


    


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
    permission_classes = [AllowAny]
