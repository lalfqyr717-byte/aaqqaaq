#!/bin/bash
set -e
python manage.py migrate --noinput
python manage.py collectstatic --noinput
# Don't run ensure_production_user.py here - it's handled in auth_login
exec gunicorn wsgi:application --bind 0.0.0.0:$PORT --workers 2 --timeout 120 --keepalive 5