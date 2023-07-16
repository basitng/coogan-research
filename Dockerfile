# Use an official Python runtime as a base image
FROM python:3.9

# Set environment variables for Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file and install the Python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django application code into the container
COPY . /app/

# Collect the static files (Optional, but recommended for production)
RUN python manage.py collectstatic --noinput

# Start the Django development server (Change the port as per your Django settings)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
