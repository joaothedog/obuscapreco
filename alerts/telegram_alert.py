import os
import requests
from dotenv import load_dotenv

# Carrega as variáveis do .env
load_dotenv()

# Token e ID do grupo (supergrupo)
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def send_telegram_alert(message):
    if not TELEGRAM_TOKEN or not TELEGRAM_CHAT_ID:
        print("🚨 TELEGRAM_TOKEN ou TELEGRAM_CHAT_ID não encontrados no .env")
        return

    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "HTML"  # permite negrito, itálico, links com <a>
    }

    try:
        response = requests.post(url, data=payload)
        if response.status_code != 200:
            print("❌ Erro ao enviar mensagem:")
            print("Código:", response.status_code)
            print("Resposta:", response.text)
        else:
            print("✅ Alerta enviado com sucesso.")
    except Exception as e:
        print("🚨 Exceção ao tentar enviar mensagem:", str(e))
