
from telethon import TelegramClient, events
import os
import asyncio

# === CONFIGURAÇÕES ===
api_id = 20225004
api_hash = "8f4c78e858658cd2aa21967a087bf819"
phone_number = "+5519971432718"
canal_origem = "https://t.me/+9sh5Is4Ytt5hMzYx"
canal_destino = "https://t.me/+pHVeR_oSuldmMzFh"

client = TelegramClient('sessao_usuario', api_id, api_hash)

async def main():
    await client.start(phone=phone_number)
    print("Bot iniciado e monitorando o canal de origem...")

    @client.on(events.NewMessage(chats=canal_origem))
    async def handler(event):
        try:
            await client.send_message(canal_destino, event.message)
            print("Mensagem replicada.")
        except Exception as e:
            print("Erro ao replicar mensagem:", e)

    await client.run_until_disconnected()

if __name__ == "__main__":
    with client:
        client.loop.run_until_complete(main())
