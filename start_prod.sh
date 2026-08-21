#!/bin/sh
set -e
# Production startup script for Railway
python manage.py migrate --noinput
python manage.py collectstatic --noinput
exec gunicorn wsgi:application --bind 0.0.0.0:${PORT:-8080} --workers 2