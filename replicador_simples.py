import re
from telethon.sync import TelegramClient, events
from telethon.tl.functions.messages import (
    ImportChatInviteRequest,
    CheckChatInviteRequest
)

# === CONFIGURAÇÕES ===
api_id    = 20225004
api_hash  = "8f4c78e858658cd2aa21967a087bf819"
SESSAO    = 'sessao_usuario'
LINK_ORIG = 'https://t.me/+XkWYvpDc2-c5ZGQ5'
LINK_DEST = 'https://t.me/+RDbY2XIDf-kyNDlh'

def iniciar_replicador():
    client = TelegramClient(SESSAO, api_id, api_hash)
    client.start()
    print("[LOG] Sessão Telegram iniciada.")

    def ensure_join(link, role):
        m = re.search(r't\.me/\+(.*)', link)
        if m:
            invite_hash = m.group(1)
            try:
                # Checa se já é membro:
                info = client(CheckChatInviteRequest(invite_hash))
                # Se não for membro, faz import
                if not hasattr(info, 'chat'):
                    client(ImportChatInviteRequest(invite_hash))
                    print(f"[LOG] Entrou no canal {role}.")
            except Exception as e:
                print(f"[ERRO] Não conseguiu entrar no {role}: {e}")

    # Garante que a instância entre nos dois canais
    ensure_join(LINK_ORIG, "origem")
    ensure_join(LINK_DEST, "destino")

    # Resolve entidades já tendo membro
    origin = client.get_entity(LINK_ORIG)
    dest   = client.get_entity(LINK_DEST)
    print(f"[LOG] Origin: {origin.title} ({origin.id})")
    print(f"[LOG] Dest:   {dest.title} ({dest.id})")

    @client.on(events.NewMessage(chats=origin))
    async def handler(ev):
        text = ev.message.text or "<sem texto>"
        print(f"[LOG] Nova msg de {origin.title}: {text}")
        try:
            await client.send_message(dest, ev.message)
            print(f"[LOG] Replicada para {dest.title}")
        except Exception as e:
            print(f"[ERRO] Falha ao replicar: {e}")

    print("[LOG] Replicador ativo. Aguardando mensagens…")
    client.run_until_disconnected()

if __name__ == "__main__":
    iniciar_replicador()
