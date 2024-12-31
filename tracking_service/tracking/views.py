from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import UserActivity, HealthMetrics
from .serializers import UserActivitySerializer, HealthMetricsSerializer

#user activities
@api_view(['GET', 'POST'])
def user_activity_list(request):
    if request.method == 'GET':
        activities = UserActivity.objects.all()
        serializer = UserActivitySerializer(activities, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserActivitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def user_activity_detail(request, pk):
    try:
        activity = UserActivity.objects.get(pk=pk)
    except UserActivity.DoesNotExist:
        return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserActivitySerializer(activity)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserActivitySerializer(activity, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        activity.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#health-metrics
@api_view(['GET', 'POST'])
def health_metrics_list(request):
    if request.method == 'GET':
        metrics = HealthMetrics.objects.all()
        serializer = HealthMetricsSerializer(metrics, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = HealthMetricsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def health_metrics_detail(request, pk):
    try:
        metric = HealthMetrics.objects.get(pk=pk)
    except HealthMetrics.DoesNotExist:
        return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = HealthMetricsSerializer(metric)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = HealthMetricsSerializer(metric, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        metric.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
