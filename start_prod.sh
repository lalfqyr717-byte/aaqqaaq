#!/bin/bash
set -e
# Entrypoint for production: run migrations, collect static, create user, then start gunicorn
cd /app
# Apply migrations (non-interactive)
python tox/manage.py migrate --noinput || true
# Collect static files
python tox/manage.py collectstatic --noinput || true
# Create or update maqi user
python create_production_user.py || true
# Start gunicorn; PORT env var is provided by Railway
exec gunicorn tox.wsgi:application --bind 0.0.0.0:${PORT:-8080} --workers 2