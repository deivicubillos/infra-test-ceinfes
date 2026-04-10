import logging
from logging.handlers import RotatingFileHandler

# Configuración de Logs Claros
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    handlers=[
        RotatingFileHandler("logs/app.log", maxBytes=10000, backupCount=3),
        logging.StreamHandler() # Esto permite verlos también con 'docker logs'
    ]
)

from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return f"Hello from {os.getenv('ENV', 'dev')}!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
