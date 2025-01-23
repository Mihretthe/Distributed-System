# Dockerfile for the Tracking Service
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Expose the tracking service port
EXPOSE 8002

# Run the Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8002"]
