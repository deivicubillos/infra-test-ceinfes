##FROM python:3.10
##WORKDIR /app
##COPY . .
##RUN pip install -r requirements.txt
##CMD ["python", "app.py"]

#[NUEVO DOCKERFILE MEJORADO EN SEGURIDAD Y PESO]

# Imagen base ligera (Slim)
FROM python:3.10-slim

# Evita que Python genere archivos .pyc y asegura logs en tiempo real
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Instalamos dependencias (Capa de caché optimizada)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el código
COPY . .

# SEGURIDAD: Usuario no-root para que un atacante no tome control del host
RUN adduser --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

# EJECUCIÓN
CMD ["python", "app.py"]
