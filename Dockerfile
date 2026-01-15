# Imagen base de Python
FROM python:3.11-slim

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar todo el proyecto al contenedor
COPY . .

# Comando que se ejecuta al iniciar el contenedor
CMD ["python3", "app/main.py"]