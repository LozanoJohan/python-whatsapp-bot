import requests
import json

phone_number_id = 400692489794103
url = f'https://graph.facebook.com/v20.0/{phone_number_id}/messages'
access_token = 'EAAGgx3lKGfQBO4R3mA16iRxhR6tEfaFOeO7xtaDEqRYlifeWTgZBFMLZAS5ZCcvJqYG78ZCcpkWFY8fdw4C6qZApuVzpwZAkG3opo6ezGzhpC4XsJEDm3mP8m1jzXS44bXZAAQpewRMSC0NKAX1eTWYrevvA3idFub6TmeZC1k9UELrgZCIfVjxI9iOBm5ZA6fL8yj8ylwYVAebaMz50kbPQZDZD'
headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json'
}

data = {
    "messaging_product": "whatsapp",
    "to": "whatsapp:+573142968931",
    "type": "interactive",
    "interactive": {
        "type": "button",
        "body": {
            "text": "¿Cómo podemos ayudarte?"
        },
        "action": {
            "buttons": [
                {
                    "type": "reply",
                    "reply": {
                        "id": "help_1",
                        "title": "Soporte"
                    }
                },
                {
                    "type": "reply",
                    "reply": {
                        "id": "help_2",
                        "title": "Información"
                    }
                }
            ]
        }
    }
}

response = requests.post(url, headers=headers, data=json.dumps(data))

print(response.status_code)
print(response.json())


import requests
import json

url = f'https://graph.facebook.com/v20.0/{phone_number_id}/messages'

headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json'
}

data = {
    "messaging_product": "whatsapp",
    "to": "573142968931",
    "type": "text",
    "text": {
        "body": "Hola, este es un mensaje de prueba."
    }
}

response = requests.post(url, headers=headers, data=json.dumps(data))

print(response.status_code)
print(response.json())





import requests
import json

url = 'https://graph.facebook.com/v16.0/400692489794103/messages'
access_token = 'EAAGgx3lKGfQBO4R3mA16iRxhR6tEfaFOeO7xtaDEqRYlifeWTgZBFMLZAS5ZCcvJqYG78ZCcpkWFY8fdw4C6qZApuVzpwZAkG3opo6ezGzhpC4XsJEDm3mP8m1jzXS44bXZAAQpewRMSC0NKAX1eTWYrevvA3idFub6TmeZC1k9UELrgZCIfVjxI9iOBm5ZA6fL8yj8ylwYVAebaMz50kbPQZDZD'  # Tu Access Token de Meta

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {access_token}'
}

data = {
    "messaging_product": "whatsapp",
    "recipient_type": "individual",
    "to": "573142968931",  # Tu número en formato internacional
    "type": "template",
    "template": {
        "name": "order_delivery_update",
        "language": {
            "code": "en_US"
        },
        "components": [
            {
                "type": "header",
                "parameters": [
                    {
                        "type": "location",
                        "location": {
                            "latitude": "37.483307",
                            "longitude": "-122.148981",
                            "name": "Pablo Morales",
                            "address": "1 Hacker Way, Menlo Park, CA 94025"
                        }
                    }
                ]
            },
            {
                "type": "body",
                "parameters": [
                    {
                        "type": "text",
                        "text": "Pablo"
                    },
                    {
                        "type": "text",
                        "text": "566701"
                    }
                ]
            }
        ]
    }
}

response = requests.post(url, headers=headers, data=json.dumps(data))

print(response.status_code)
print(response.json())
