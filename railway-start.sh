#!/bin/bash
set -e
python manage.py migrate --noinput
python manage.py collectstatic --noinput
python ensure_production_user.py
exec gunicorn wsgi:application --bind 0.0.0.0:$PORT --workers 2