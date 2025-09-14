import os
import time
from flask import Flask, request, jsonify, send_from_directory, url_for
from gtts import gTTS
from dotenv import load_dotenv
import requests

load_dotenv()

# Groq API setup
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

app = Flask(__name__)

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    farmer_query = data.get("query", "")

    # Call Groq API
    headers = {"Authorization": f"Bearer {GROQ_API_KEY}"}
    payload = {
        "model": "llama-3.1-8b-instant",
        "messages": [
            {"role": "system", "content": "You are KisanMitra, an AI assistant for Indian farmers. Respond in simple English with actionable advice. Include: diagnosis, recommended pesticides, and government schemes if relevant."},
            {"role": "user", "content": farmer_query}
        ]
    }

    resp = requests.post(GROQ_API_URL, headers=headers, json=payload)
    resp_data = resp.json()
    answer = resp_data["choices"][0]["message"]["content"]

    # Save audio response
    audio_filename = f"response_{int(time.time())}.mp3"
    audio_path = os.path.join("static", audio_filename)
    tts = gTTS(answer, lang="en")
    tts.save(audio_path)

    # Generate full audio URL for Streamlit
    audio_url = url_for("serve_audio", path=audio_filename, _external=True)

    return jsonify({
        "query": farmer_query,
        "answer": answer,
        "audio": audio_url
    })

@app.route("/static/<path:path>")
def serve_audio(path):
    return send_from_directory("static", path)

if __name__ == "__main__":
    os.makedirs("static", exist_ok=True)
    app.run(debug=True)
