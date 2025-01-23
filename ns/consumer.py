# notifications/consumer.py
import pika
import json
from datetime import datetime, timedelta

DAILY_GOALS = {
    "steps": 10000,
    "distance_km": 5,
    "calories_burned": 2000,
}

def process_message(channel, method, properties, body):
    """
    Process a single RabbitMQ message and create a notification if needed.
    """
    data = json.loads(body)
    user_id = data["user_id"]
    steps = data["steps"]
    distance_km = data["distance_km"]
    calories_burned = data["calories_burned"]
    date = datetime.strptime(data["date"], "%Y-%m-%d").date()

    # Check if the user reached their goals
    if steps >= DAILY_GOALS["steps"] or distance_km >= DAILY_GOALS["distance_km"] or calories_burned >= DAILY_GOALS["calories_burned"]:
        message = "🎉 Congratulations! You've reached your daily goal! Keep it up!"
    else:
        current_time = datetime.now()
        end_of_day = datetime.combine(date, datetime.max.time())
        time_remaining = (end_of_day - current_time).seconds

        if time_remaining < 3600:  # Less than 1 hour remaining
            message = "⏳ The day is almost over! Keep pushing to reach your daily goal—you can do it!"
        else:
            return  # No notification needed yet

    # Save notification to the database
    Notification.objects.create(user_id=user_id, message=message)

def start_consumer():
    """
    Start the RabbitMQ consumer for processing user activity messages.
    """
    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    channel = connection.channel()

    channel.queue_declare(queue="user_activity")
    channel.basic_consume(
        queue="user_activity",
        on_message_callback=process_message,
        auto_ack=True,
    )

    print(" [*] Waiting for messages. To exit press CTRL+C")
    channel.start_consuming()
