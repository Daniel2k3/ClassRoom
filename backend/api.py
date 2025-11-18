from flask import Flask, request
from extractor import extract_text
from ai_generator import generate_study_materials
from pdf_converter import convert_to_pdf
import requests
from config import WEBEX_TOKEN
import os

app = Flask(__name__)

def send_file_back(room_id, filepath):
    requests.post(
        "https://webexapis.com/v1/messages",
        headers={"Authorization": f"Bearer {WEBEX_TOKEN}"},
        data={"roomId": room_id, "text": "🎉 Your materials are ready!"},
        files={"files": open(filepath, "rb")}
    )

@app.post("/process")
def process():
    data = request.json
    file_url = data["file_url"]
    room_id = data["room_id"]

    # Download input file
    r = requests.get(file_url, headers={"Authorization": f"Bearer {WEBEX_TOKEN}"})
    with open("input_file", "wb") as f:
        f.write(r.content)

    # Extract text
    clean_text = extract_text("input_file")

    # Generate materials
    guide, summary, quiz = generate_study_materials(clean_text)

    # Save materials
    os.makedirs("output", exist_ok=True)
    open("output/study_guide.txt", "w").write(guide)
    open("output/summary.txt", "w").write(summary)
    open("output/quiz.txt", "w").write(quiz)

    # Convert to PDF
    convert_to_pdf("output/study_guide.txt", "output/study_guide.pdf")
    convert_to_pdf("output/summary.txt", "output/summary.pdf")
    convert_to_pdf("output/quiz.txt", "output/quiz.pdf")

    # Send PDFs back
    send_file_back(room_id, "output/study_guide.pdf")
    send_file_back(room_id, "output/summary.pdf")
    send_file_back(room_id, "output/quiz.pdf")

    return "OK", 200

app.run(port=5001)