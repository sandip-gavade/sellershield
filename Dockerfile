# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Install PostgreSQL development libraries
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    gcc

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app/

# Install the dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Expose the Django port
EXPOSE 8000

# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
