import streamlit as st
import requests

st.title("🚜 KisanMitra – AI Farming Assistant")

query = st.text_input("Farmer, please enter your question:")

if st.button("Ask"):
    if query:
        try:
            resp = requests.post("http://127.0.0.1:5000/ask", json={"query": query})
            data = resp.json()

            st.subheader("🩺 Diagnosis / Answer")
            st.success(data["answer"])

            st.subheader("🔊 Listen to the Answer")
            st.audio(data["audio"])
        except Exception as e:
            st.error(f"⚠️ Something went wrong: {e}")
    else:
        st.warning("Please type your question before clicking Ask.")
