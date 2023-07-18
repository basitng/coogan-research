# Use an official Python runtime as a base image
FROM python:3.11.4-alpine


# Set the working directory inside the container
WORKDIR /usr/src/app/

# Set environment variables for Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# Copy the requirements.txt file and install the Python dependencies
RUN pip install --upgrade pip
COPY requirements.txt /usr/src/app/requirements.txt


RUN pip install -r requirements.txt