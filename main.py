from fastapi import FastAPI, WebSocket
from fastapi.responses import JSONResponse
from models import devil_light, devil_iq
from tts import generate_tts
from logo_gen import generate_logo

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Devil AI Chat Running!"}

# WebSocket for real-time chat
@app.websocket("/ws")
async def websocket_endpoint(ws: WebSocket):
    await ws.accept()
    while True:
        data = await ws.receive_json()
        user_message = data["message"]
        model = data.get("model", "DEVIL_LIGHT")

        if model == "DEVIL_LIGHT":
            response = devil_light(user_message)
        else:
            response = devil_iq(user_message)

        await ws.send_json({"response": response})

# TTS endpoint
@app.post("/tts")
async def tts_api(text: str):
    audio_url = generate_tts(text)
    return JSONResponse({"audio_url": audio_url})

# Logo Gen endpoint
@app.post("/logo")
async def logo_api(prompt: str):
    logo_url = generate_logo(prompt)
    return JSONResponse({"logo_url": logo_url})