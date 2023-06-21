# Utiliza la imagen base de Python
FROM python:3.9-slim

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia los archivos necesarios al contenedor
COPY app.py /app
COPY requirements.txt /app

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Instalar curl
RUN apt-get update && apt-get install -y curl

# Crea un usuario no root
RUN useradd -m -U python

# Cambia la propiedad del directorio de trabajo al usuario no root
RUN chown -R python:python /app

# Cambia al usuario no root
USER python

# Expone el puerto 8080
EXPOSE 8080

# Ejecuta la aplicación Flask
CMD ["python", "app.py"]