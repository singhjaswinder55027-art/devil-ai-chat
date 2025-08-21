import requests

def generate_tts(text):
    # Replace with your TTS API
    url = "https://api.streamelements.com/kappa/v2/speech?voice=brian"
    res = requests.post(url, json={"text": text})
    return res.json().get("audio_url", "")