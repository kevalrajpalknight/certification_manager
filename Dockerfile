# Use an official Python runtime as a parent image
FROM python:3.10

# Set environment variables for Django
ENV DJANGO_SETTINGS_MODULE project.settings
ENV DJANGO_SECRET_KEY your-secret-key

# Set environment variables for Redis
ENV REDIS_HOST redis
ENV REDIS_PORT 6379

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make the entrypoint script executable
RUN chmod +x /app/entrypoint.sh

# Expose port 8000 for the Django application
EXPOSE 8000

# Start the custom entrypoint script
CMD ["/app/entrypoint.sh"]
