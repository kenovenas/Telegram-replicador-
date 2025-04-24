from flask import Flask
import asyncio
import threading
from replicador_simples import main, client

app = Flask(__name__)

loop = asyncio.new_event_loop()

def start_bot():
    asyncio.set_event_loop(loop)
    with client:
        loop.run_until_complete(main())

@app.before_first_request
def activate_bot():
    thread = threading.Thread(target=start_bot)
    thread.start()

@app.route('/')
def home():
    return "Servidor do replicador do Telegram está rodando."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
