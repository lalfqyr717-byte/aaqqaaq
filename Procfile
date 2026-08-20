web: python manage.py migrate --noinput && python manage.py collectstatic --noinput && gunicorn toxerp.wsgi:application --bind 0.0.0.0:${PORT:-8000} --workers ${GUNICORN_WORKERS:-4}
