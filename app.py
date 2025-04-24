from flask import Flask
from replicador_simples import iniciar_replicador
import threading
import os

app = Flask(__name__)

@app.route('/')
def home():
    return 'Replicador ativo!'

# Iniciar o replicador imediatamente, sem esperar por requisição
threading.Thread(target=iniciar_replicador, daemon=True).start()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
