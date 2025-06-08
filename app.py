import streamlit as st
from utils.speech_utils import recognize_speech, synthesize_speech
from utils.emotion_utils import analyze_sentiment
from dotenv import load_dotenv
import os

load_dotenv()

st.title("🎙️ Emotion Voice Chatbot")
st.markdown("Speak English. The bot will understand your emotion and respond with voice!")

if st.button("🎤 Start Talking"):
    with st.spinner("Listening..."):
        text = recognize_speech()
        if not text:
            st.error("Could not recognize speech.")
            st.stop()
        st.success(f"You said: {text}")

    sentiment = analyze_sentiment(text)
    st.info(f"Detected sentiment: **{sentiment.upper()}**")

    # 固定回應
    if sentiment == "positive":
        reply = "I'm glad you're feeling good today!"
    elif sentiment == "negative":
        reply = "I'm sorry to hear that. I'm here if you want to talk."
    else:
        reply = "Thanks for sharing. I'm listening."

    st.write(f"🤖 Bot: {reply}")
    synthesize_speech(reply)
    st.audio("static/response.mp3")
