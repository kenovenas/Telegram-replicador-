import re
import asyncio
from telethon.sync import TelegramClient, events
from telethon.tl.functions.messages import ImportChatInviteRequest

# === Configurações ===
api_id = 20225004
api_hash = "8f4c78e858658cd2aa21967a087bf819"
SESSAO = 'sessao_usuario'
LINK_ORIG = 'https://t.me/+qBGna2cSfSI1ZWQx'
LINK_DEST = 'https://t.me/+RDbY2XIDf-kyNDlh'

def extrair_hash(link):
    match = re.search(r't\.me/\+([a-zA-Z0-9_-]+)', link)
    if match:
        return match.group(1)
    return None

def entrar_por_link(client, link, tipo):
    invite_hash = extrair_hash(link)
    if not invite_hash:
        print(f"[ERRO] Link inválido: {link}")
        return None
    try:
        print(f"[LOG] Tentando entrar no {tipo} via convite...")
        client(ImportChatInviteRequest(invite_hash))
        print(f"[LOG] Entrou no {tipo} com sucesso.")
    except Exception as e:
        print(f"[LOG] Já está no {tipo} ou erro ao entrar: {e}")
    return client.get_entity(link)

def iniciar_replicador():
    # CORREÇÃO: cria e define o event loop na thread
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    client = TelegramClient(SESSAO, api_id, api_hash)
    client.start()
    print("[LOG] Sessão iniciada.")

    origem = entrar_por_link(client, LINK_ORIG, "origem")
    destino = entrar_por_link(client, LINK_DEST, "destino")

    if not origem or not destino:
        print("[ERRO] Não foi possível resolver os links.")
        return

    print(f"[LOG] Canal origem: {origem.title} ({origem.id})")
    print(f"[LOG] Canal destino: {destino.title} ({destino.id})")

    @client.on(events.NewMessage(chats=origem))
    async def handler(event):
        texto = event.message.text or "<sem texto>"
        print(f"[RECEBIDO] {texto}")
        try:
            await client.send_message(destino, event.message)
            print("[ENVIADO] Mensagem replicada com sucesso.")
        except Exception as e:
            print(f"[ERRO] Falha ao enviar mensagem: {e}")

    print("[LOG] Replicador ativo e escutando...")
    client.run_until_disconnected()

if __name__ == "__main__":
    iniciar_replicador()
