import streamlit as st 
import google.generativeai as genai

st.title("Machine Translation")
sentance = st.text_input("Enter The Sentance for Sentiment analysis", "")
button  = st.button("Response")

prompt = "Translate the sentance in Hindi language and Spanish Language both"

key = "AIzaSyC_L3-d181ibSultwSEuGm6P4XwE8HIsEQ"
genai.configure(api_key=key)

if button:
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt, sentance])
    st.markdown(response.text)
