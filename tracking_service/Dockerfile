# Use a lightweight Python image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container
COPY . .

# Set the default command to run the Django app using Gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:8000", "tracking_service.wsgi:application"]
