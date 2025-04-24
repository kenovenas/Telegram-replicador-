from flask import Flask
from replicador_simples import iniciar_replicador
import threading

app = Flask(__name__)

@app.route('/')
def home():
    return 'Servidor Flask do replicador está rodando!'

if __name__ == '__main__':
    try:
        threading.Thread(target=iniciar_replicador).start()
        app.run(host='0.0.0.0', port=10000)
    except Exception as e:
        print('[ERRO AO INICIAR BOT]')
        print(e)
