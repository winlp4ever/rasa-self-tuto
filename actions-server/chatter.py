import requests

res = requests.post('http://localhost:5005/webhooks/rest/webhook', json={
    "message":"c'est quoi html", 
    "sender": "quang"
})

print(res.json())