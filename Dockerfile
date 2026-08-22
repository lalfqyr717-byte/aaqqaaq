FROM python:3.12-slim

WORKDIR /app

ENV ALLOWED_HOSTS=127.0.0.1,localhost,moq.up.railway.app,moqq.up.railway.app,healthcheck.railway.app
ENV TOX_DEBUG=False
ENV DJANGO_SETTINGS_MODULE=tox.settings
ENV PORT=8080

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Make sure Django settings are correct
RUN python manage.py check --deploy

CMD sh -c "python manage.py migrate --noinput && python manage.py collectstatic --noinput && gunicorn wsgi:application --bind 0.0.0.0:${PORT} --workers 2 --timeout 120 --keepalive 5"