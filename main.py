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