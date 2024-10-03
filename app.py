from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

WHATSAPP_NUMBER = "410703692131187"
ACCESS_TOKEN = "EAAHRCGz6XnkBOZB23aE8HyrBFFGw2tS6P4TBWysfQDkfQXxItdj0L5t3QzZANKMEriCgDHDzVnwZCrmACfQgq9Y4vUMwXZBVfgrbRufPlCiYZC4b0FyzZCqWUqwSdfNCpDwojUjyCAw8ZCd76gcyFNZBhXrAKMChsEgZBZCUwmFRCsGw3rorholJ2giOzrc5fUJo7m3KooIAZCqz1waVTPVdIdjaHY4ucvX7ZAgNOgZDZD"



@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.json

    numero_destino = data.get('to')
    mensaje = data.get('message')

    if not numero_destino or not mensaje:
        return jsonify({"error": "Número de destino y mensaje son requeridos"}), 400

    url = f"https://graph.facebook.com/v21.0/{WHATSAPP_NUMBER}/messages"

    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }

    payload = {
        "messaging_product": "whatsapp",
        "to": numero_destino,
        "type": "text",
        "text": {
            "body": mensaje
        }
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        return jsonify({"message": "Mensaje enviado correctamente"}), 200
    else:
        return jsonify({"error": "Error al enviar el mensaje", "details": response.json()}), response.status_code


if __name__ == '__main__':
    app.run(debug=True)
