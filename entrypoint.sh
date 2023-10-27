#!/bin/bash
# Start Gunicorn with --reload for code changes
gunicorn --reload --bind 0.0.0.0:8000 project.wsgi:application &

# Watch for code changes and apply migrations
watchmedo auto-restart --directory /app --pattern *.py --recursive python manage.py migrate

# Keep the script running to maintain both processes
tail -f /dev/null
