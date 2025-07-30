from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7837949074:AAG5uYE0TtVQBFSKTp9AIc8PqvlcoY1G2RY")
BOT_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

@app.route('/', methods=['GET'])
def index():
    return 'Bot aktif dan siap cuan!'

@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()

    if 'message' in data:
        chat_id = data['message']['chat']['id']
        text = data['message'].get('text', '')

        if text == '/start':
            msg = "👋 Halo! Bot AgushCuan aktif!\nKetik /token buat dapet notifikasi token baru dari Pump.fun 🚀"
        elif text == '/token':
            msg = "🔔 Fitur notifikasi token baru sedang disiapkan, ditunggu ya!"
        else:
            msg = "❓ Perintah tidak dikenal. Coba ketik /start atau /token."

        requests.post(BOT_URL, json={"chat_id": chat_id, "text": msg})

    return '', 200

if __name__ == '__main__':
    app.run(debug=True)
