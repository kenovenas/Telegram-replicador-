from flask import Flask
import threading
from replicador_simples import main  # Usamos a função principal corretamente

app = Flask(__name__)

@app.route('/')
def home():
    return 'Servidor replicador está rodando!'

def iniciar_bot():
    main()

# Iniciar o bot em thread separada
threading.Thread(target=iniciar_bot).start()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
