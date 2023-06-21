from flask import Flask, jsonify
import time
import os

app = Flask(__name__)

@app.route('/api')
def process_sleep():
    sleep_value = read_sleep_value()
    
    if sleep_value is None:
        return jsonify({'error': 'El archivo no existe'}), 500
    
    if not sleep_value.isdigit():
        return jsonify({'error': 'El valor no es numérico'}), 500
    
    sleep_value = int(sleep_value)
    time.sleep(sleep_value)
    
    version = os.environ.get('VERSION', 'undefined')  # Obtener el valor de la variable de entorno "version" o asignar 'undefined' si no existe

    return jsonify({'message': f'Holis, dormi {sleep_value} segundos', 'version': version})

def read_sleep_value():
    sleep_file = '/tmp/sleep'
    
    if os.path.exists(sleep_file):
        with open(sleep_file, 'r') as file:
            return file.read().strip()
    
    return '0'

if __name__ == '__main__':
    app.run(port=8080)