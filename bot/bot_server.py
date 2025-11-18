from flask import Flask, request
import requests
import json
from webex_api import send_message, download_file
from config import WEBEX_TOKEN
import os

app = Flask(__name__)

BACKEND_URL = "http://localhost:5001/process"

@app.post("/webhook")
def webhook():

    data = request.json
    message_id = data["data"]["id"]

    # Get full message
    msg = requests.get(
        f"https://webexapis.com/v1/messages/{message_id}",
        headers={"Authorization": f"Bearer {WEBEX_TOKEN}"}
    ).json()

    room_id = msg["roomId"]

    # If user uploaded a file
    if "files" in msg:
        file_url = msg["files"][0]

        send_message(room_id, "📄 File received! Extracting text…")

        # Pass file URL to backend
        requests.post(BACKEND_URL, json={
            "file_url": file_url,
            "room_id": room_id
        })

        return "OK", 200

    else:
        send_message(room_id, "Please upload a PDF or PPTX file.")
        return "NO FILE", 200


if __name__ == "__main__":
    app.run(port=5000)