#!/bin/bash

# Apply database migrations
PYTHONDONTWRITEBYTECODE=1 python ./manage.py migrate --noinput

# Start celery worker
celery -A dudashop worker --loglevel=INFO &

# Run server
PYTHONDONTWRITEBYTECODE=1  python ./manage.py runserver 0.0.0.0:8000 
