from flask import Flask
from threading import Thread
from replicador_simples import iniciar_replicador
import os

app = Flask(__name__)

@app.route('/')
def home():
    return 'Replicador ativo!'

def start_replicador():
    try:
        iniciar_replicador()
    except Exception as e:
        print(f"[ERRO AO INICIAR REPLICADOR] {e}")

if __name__ == '__main__':
    Thread(target=start_replicador).start()
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
