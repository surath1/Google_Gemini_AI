from dotenv import load_dotenv
load_dotenv() #load all env veriables

# Import library
import os
import streamlit as st

import pathlib
import textwrap
import google.generativeai as genai

# Configure 
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)


model = genai.GenerativeModel('gemini-pro')

response = model.generate_content("What is the GDP of USA?")

print(response.text)
#print(response.prompt_feedback)
#print(response.candidates)

def get_response_gemini_pro(question):
    response = model.generate_content(question)
    return response.text


st.set_page_config(page_title='Gemini AI Q&A')
st.header("Google Gemini AI ")
input = st.text_input("Input:", key='input')
submit = st.button("Question?")

if submit:
    response = get_response_gemini_pro(input)
    st.write(response)


