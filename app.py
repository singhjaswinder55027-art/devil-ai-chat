from flask import Flask, render_template, request, jsonify
from models import devil_light, devil_iq
from tts import generate_tts
from logo_gen import generate_logo

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

# Chat endpoint
@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    message = data.get("message")
    model = data.get("model")

    if model == "DEVIL LIGHT 1.0":
        reply = devil_light(message)
    elif model == "DEVIL IQ 1.5":
        reply = devil_iq(message)
    else:
        reply = "❌ Unknown model."

    return jsonify({"reply": reply})

# TTS endpoint
@app.route("/tts", methods=["POST"])
def tts():
    data = request.json
    text = data.get("text")
    audio_url = generate_tts(text)
    return jsonify({"audio_url": audio_url})

# Logo Generation endpoint
@app.route("/logo", methods=["POST"])
def logo():
    data = request.json
    prompt = data.get("prompt")
    img_url = generate_logo(prompt)
    return jsonify({"logo_url": img_url})

if __name__ == "__main__":
    app.run(debug=True)