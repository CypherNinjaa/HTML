from flask import Flask, request
import requests

app = Flask(__name__)

# Telegram Bot Credentials
BOT_TOKEN = "8156841245:AAF6iJLgxvI5VnpaMrWFyCNOYKhPEUYix3s"
CHAT_ID = "-4640834480"

@app.route("/sendMessage", methods=["POST"])
def send_message():
    # Get form data
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")

    # Format the message
    text = f"📩 *New Form Submission*\n\n👤 *Name:* {name}\n📧 *Email:* {email}\n📝 *Message:* {message}"

    # Telegram API URL
    telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    
    payload = {
        "chat_id": CHAT_ID,
        "text": text,
        "parse_mode": "Markdown",
    }

    # Send request to Telegram
    response = requests.post(telegram_url, data=payload)

    if response.ok:
        return "Message sent successfully!"
    else:
        return "Failed to send message.", 500

if __name__ == "__main__":
    app.run(debug=True)
