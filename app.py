from flask import Flask, make_response, jsonify
import time
import os
import socket
import datetime
import random
import requests

app = Flask(__name__)

@app.route('/api')
def process_sleep():
    sleep_value = read_sleep_value()
    urls = [
        "http://www.google.com",
        "http://www.yahoo.com",
        "http://www.example.com",
        "http://www.openai.com",
        "http://www.python.org",
        "http://www.github.com",
        "http://www.stackoverflow.com",
        "http://www.medium.com",
        "http://www.amazon.com",
        "http://www.microsoft.com"
    ]
    url = random.choice(urls)
    response = requests.get(url)

    if sleep_value is None:
        return jsonify({'error': 'El archivo no existe'}), 500
    
    if not sleep_value.isdigit():
        return jsonify({'error': 'El valor no es numérico'}), 500
    
    sleep_value = int(sleep_value)
    time.sleep(sleep_value)
    
    # Obtener el hostname
    hostname = socket.gethostname()

    version = os.environ.get('VERSION', 'undefined')  # Obtener el valor de la variable de entorno "version" o asignar 'undefined' si no existe

    fecha_actual = datetime.datetime.now()
    
    return make_response(jsonify({'message': f'Holis, dormi {sleep_value} segundos', 'version': version, 'hostname': hostname, 'fecha_actual': fecha_actual, 'url': url, 'status_code': response.status_code}), response.status_code)

def read_sleep_value():
    sleep_file = '/tmp/sleep'
    
    if os.path.exists(sleep_file):
        with open(sleep_file, 'r') as file:
            return file.read().strip()
    
    return '0'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)