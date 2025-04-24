from flask import Flask
import asyncio
import threading
import os
from replicador_simples import main, client

app = Flask(__name__)
loop = asyncio.new_event_loop()

def start_bot():
    try:
        print("[LOG] Iniciando bot em segundo plano...")
        asyncio.set_event_loop(loop)
        with client:
            loop.run_until_complete(main())
    except Exception as e:
        import traceback
        print("[ERRO AO INICIAR BOT]")
        traceback.print_exc()

@app.before_first_request
def activate_bot():
    print("[LOG] Flask recebeu a primeira requisição. Iniciando thread do bot.")
    thread = threading.Thread(target=start_bot)
    thread.start()

@app.route('/')
def home():
    print("[LOG] Rota raiz acessada.")
    return "Servidor do replicador do Telegram está rodando."

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    print(f"[LOG] Iniciando Flask na porta {port}")
    app.run(host='0.0.0.0', port=port)
