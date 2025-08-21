import os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

GEMINI_KEY = os.getenv("AIzaSyAPD96JXdmiQeqUC9o6SHPJpjoTl2Co2q8")

def devil_light(text):
    """ DEVIL LIGHT 1.0 → Gemini Flash model """
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={GEMINI_KEY}"
    payload = {
        "contents": [{"parts": [{"text": text}]}]
    }
    res = requests.post(url, json=payload)
    try:
        return res.json()["candidates"][0]["content"]["parts"][0]["text"]
    except Exception as e:
        return f"[DEVIL LIGHT ERROR] {str(e)}"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_input = data.get("text", "")
    
    reply = devil_light(user_input)
    
    return jsonify({
        "user_input": user_input,
        "reply": reply
    })

# Vercel ke liye handler
def handler(request, response):
    with app.request_context(request.environ):
        return app.full_dispatch_request()