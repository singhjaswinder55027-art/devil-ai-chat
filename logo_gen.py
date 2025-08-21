import requests

def generate_logo(prompt):
    # Replace with your Logo API
    url = "https://ai-image-genl.vercel.app/?prompt="
    res = requests.post(url, json={"prompt": prompt})
    return res.json().get("logo_url", "")