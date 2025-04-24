
from flask import Flask
import asyncio
from replicador_simples import main, client

app = Flask(__name__)

@app.route('/')
def home():
    return "Servidor do replicador do Telegram está rodando."

@app.route('/start')
def start_replicador():
    loop = asyncio.get_event_loop()
    loop.create_task(main())
    return "Bot iniciado!"

if __name__ == '__main__':
    with client:
        client.loop.run_until_complete(main())
