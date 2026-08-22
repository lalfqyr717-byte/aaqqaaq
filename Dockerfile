FROM python:3.12-slim

WORKDIR /app

ENV ALLOWED_HOSTS=127.0.0.1,localhost,moq.up.railway.app,moqq.up.railway.app,healthcheck.railway.app
ENV TOX_DEBUG=False
ENV DJANGO_SETTINGS_MODULE=tox.settings
ENV PORT=8080

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]