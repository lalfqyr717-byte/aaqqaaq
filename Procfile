web: cd tox && python manage.py migrate --noinput && python manage.py collectstatic --noinput && gunicorn tox.wsgi:application --bind 0.0.0.0:$PORT --workers 4
