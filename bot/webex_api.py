import requests
import json
from config import WEBEX_TOKEN

BASE_URL = "https://webexapis.com/v1"

def send_message(room_id, text):
    url = f"{BASE_URL}/messages"
    headers = {"Authorization": f"Bearer {WEBEX_TOKEN}",
               "Content-Type": "application/json"}

    payload = {"roomId": room_id, "text": text}

    requests.post(url, headers=headers, data=json.dumps(payload))


def send_file(room_id, filepath):
    url = f"{BASE_URL}/messages"
    headers = {"Authorization": f"Bearer {WEBEX_TOKEN}"}
    files = {"files": open(filepath, "rb")}
    data = {"roomId": room_id, "text": "📚 Here is your generated material!"}

    requests.post(url, headers=headers, data=data, files=files)


def download_file(url):
    res = requests.get(url, headers={"Authorization": f"Bearer {WEBEX_TOKEN}"})
    with open("input_file", "wb") as f:
        f.write(res.content)