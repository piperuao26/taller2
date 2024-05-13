# Usa la imagen base de Python
FROM python:3.9

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia los archivos necesarios a la imagen
COPY app.py .
COPY routes.py .
COPY taller2/templates/ ./taller2/templates/

# Expone el puerto 5000 para que la aplicación sea accesible
EXPOSE 5000

# Ejecuta la aplicación al iniciar el contenedor
CMD ["python", "app.py"]