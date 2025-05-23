FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    libsasl2-dev \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

# Exponer el puerto por donde Gunicorn servirá
EXPOSE 8000

# Ejecutar migraciones y luego lanzar Gunicorn
CMD ["sh", "-c", "python manage.py migrate && gunicorn arbnb.wsgi:application --bind 0.0.0.0:8000"]
