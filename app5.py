import streamlit as st
import google.generativeai as genai


st.title("Welcome to Streamlit with Gemini AI")

user_input = st.text_input("Ask me anything")

genai.configure(api_key="AIzaSyD6X-VRnmJdHsY0sTzamlZu3yoWi1Kd80U")

model = genai.GenerativeModel("models/gemini-2.5-flash")


if user_input:
    response = model.generate_content(user_input)
    st.write("Response",response.text)
