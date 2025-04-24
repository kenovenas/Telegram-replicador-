from telethon.sync import TelegramClient, events

# Configurações da sessão e canais
api_id = 20225004
api_hash = "8f4c78e858658cd2aa21967a087bf819"
SESSAO = 'sessao_usuario'
GRUPO_ORIGEM = 'https://t.me/+XkWYvpDc2-c5ZGQ5'
GRUPO_DESTINO = 'https://t.me/+RDbY2XIDf-kyNDlh'

def iniciar_replicador():
    client = TelegramClient(SESSAO, api_id, api_hash)

    @client.on(events.NewMessage(chats=GRUPO_ORIGEM))
    async def handler(event):
        try:
            mensagem = event.message
            await client.send_message(GRUPO_DESTINO, mensagem)
            print(f"Mensagem replicada: {mensagem.text}")
        except Exception as e:
            print(f"Erro ao replicar mensagem: {e}")

    client.start()
    print("Replicador iniciado...")
    client.run_until_disconnected()

if __name__ == "__main__":
    iniciar_replicador()
