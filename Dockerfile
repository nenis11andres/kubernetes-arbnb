FROM python:3.10-slim

WORKDIR /app

# Instalamos librerías necesarias para python-ldap y compilación
RUN apt-get update && apt-get install -y \
    build-essential \
    libsasl2-dev \
    python3-dev \
    libldap2-dev \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["gunicorn", "arbnb.wsgi:application", "--bind", "0.0.0.0:8000"]
