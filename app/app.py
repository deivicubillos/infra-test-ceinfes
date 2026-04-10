import os
import logging
from flask import Flask
from logging.handlers import RotatingFileHandler

app = Flask(__name__)

# --- CONFIGURACIÓN DE LOGS PROFESIONALES ---
if not os.path.exists('logs'):
    os.mkdir('logs')

file_handler = RotatingFileHandler('logs/app.log', maxBytes=10240, backupCount=10)
file_handler.setFormatter(logging.Formatter(
    '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
))
file_handler.setLevel(logging.INFO)
app.logger.addHandler(file_handler)
app.logger.setLevel(logging.INFO)
app.logger.info('App iniciando...')
# ------------------------------------------

@app.route('/')
def hello():
    env = os.getenv('ENV', 'dev')
    app.logger.info(f'Petición recibida en entorno: {env}') # Registro de cada visita
    return f"Hello from {env}!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
