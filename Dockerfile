FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONUNBUFFERED=1

CMD ["sh", "-c", "cd tox && python manage.py migrate --noinput && python manage.py collectstatic --noinput && gunicorn tox.wsgi:application --bind 0.0.0.0:$PORT --workers 4"]