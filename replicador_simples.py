from telethon.sync import TelegramClient, events

# ===== Configurações =====
api_id    = 20225004
api_hash  = "8f4c78e858658cd2aa21967a087bf819"
SESSAO    = 'sessao_usuario'
LINK_ORIG = 'https://t.me/+XkWYvpDc2-c5ZGQ5'
LINK_DEST = 'https://t.me/+RDbY2XIDf-kyNDlh'

def iniciar_replicador():
    client = TelegramClient(SESSAO, api_id, api_hash)
    print("[LOG] Usuário iniciando sessão no Telegram...")
    client.start()
    
    # Resolver links para entidades
    print(f"[LOG] Obtendo entidade de origem: {LINK_ORIG}")
    origin = client.get_entity(LINK_ORIG)
    print(f"[LOG] Obtido origin: {origin.title} ({origin.id})")
    
    print(f"[LOG] Obtendo entidade de destino: {LINK_DEST}")
    dest = client.get_entity(LINK_DEST)
    print(f"[LOG] Obtido dest: {dest.title} ({dest.id})")
    
    @client.on(events.NewMessage(chats=origin))
    async def handler(event):
        text = event.message.text or "<sem texto>"
        print(f"[LOG] Nova mensagem recebida de {origin.title}: {text}")
        try:
            await client.send_message(dest, event.message)
            print(f"[LOG] Mensagem encaminhada para {dest.title}")
        except Exception as e:
            print(f"[ERRO] Falha ao encaminhar: {e}")

    print("[LOG] Replicador ativo e ouvindo mensagens...")
    client.run_until_disconnected()

if __name__ == "__main__":
    iniciar_replicador()
