import streamlit as st
import openai
from datetime import datetime
import pytz

# Get current date and time in New York timezone
ny_tz = pytz.timezone("America/New_York")
now_ny = datetime.now(ny_tz).strftime("%A, %B %d, %Y %I:%M:%S %p")  # 12-hour format with AM/PM

# OpenRouter API base and key
openai.api_base = "https://openrouter.ai/api/v1"
openai.api_key = st.secrets["openrouter_key"]

st.title("AI Chatbot")

# Code for input form
with st.form("chat_form"):
    user_input = st.text_input("Ask anything:")
    submitted = st.form_submit_button("Get Response")

if submitted and user_input:
    response = openai.ChatCompletion.create(
        model="mistralai/mistral-7b-instruct:free",  # Free model ID
        messages=[
            {"role": "system", "content": f"Today’s date and time in New York is {now_ny}. You are a helpful assistant."},
            {"role": "user", "content": user_input}
        ]
    )
    st.write("Bot:", response.choices[0].message.content)

