from flask import Flask, request, jsonify
from models import devil_light, devil_iq
from tts import generate_tts
from logo_gen import generate_logo

app = Flask(__name__)

@app.route("/", methods=["GET"])
def health():
    return jsonify({"message": "Devil AI Bot is alive!"})

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json() or {}
    msg = data.get("message", "")
    model = data.get("model", "DEVIL_LIGHT")
    resp = devil_light(msg) if model == "DEVIL_LIGHT" else devil_iq(msg)
    return jsonify({"reply": resp})

@app.route("/tts", methods=["POST"])
def tts_api():
    text = (request.get_json() or {}).get("text", "")
    url = generate_tts(text)
    return jsonify({"audio_url": url})

@app.route("/logo", methods=["POST"])
def logo_api():
    prompt = (request.get_json() or {}).get("prompt", "")
    url = generate_logo(prompt)
    return jsonify({"logo_url": url})

# Vercel handler
def handler(request, response):
    return app(request.environ, response.start_response)