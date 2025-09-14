import os
import time
import streamlit as st
from gtts import gTTS
from dotenv import load_dotenv
import requests

# Load API key
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

st.title("🚜 KisanMitra – AI Farming Assistant")

query = st.text_input("Farmer, please enter your question:")

if st.button("Ask"):
    if query:
        try:
            # Call Groq API directly
            headers = {"Authorization": f"Bearer {GROQ_API_KEY}"}
            payload = {
                "model": "llama-3.1-8b-instant",
                "messages": [
                    {"role": "system", "content": "You are KisanMitra, an AI assistant for Indian farmers. Respond in simple English with actionable advice. Include: diagnosis, recommended pesticides, and government schemes if relevant."},
                    {"role": "user", "content": query}
                ]
            }

            resp = requests.post(GROQ_API_URL, headers=headers, json=payload)
            resp_data = resp.json()
            answer = resp_data["choices"][0]["message"]["content"]

            # Show text answer
            st.subheader("🩺 Diagnosis / Answer")
            st.success(answer)

            # Convert to audio
            audio_filename = f"response_{int(time.time())}.mp3"
            tts = gTTS(answer, lang="en")
            tts.save(audio_filename)

            # Play audio in Streamlit
            st.subheader("🔊 Listen to the Answer")
            with open(audio_filename, "rb") as f:
                st.audio(f.read(), format="audio/mp3")

        except Exception as e:
            st.error(f"⚠️ Something went wrong: {e}")
    else:
        st.warning("Please type your question before clicking Ask.")
