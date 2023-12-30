from dotenv import load_dotenv
load_dotenv() #load all env veriables

# Import library
import os
import streamlit as st
import pathlib
import textwrap
import google.generativeai as genai
from PIL import Image

# Configure 
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)


model = genai.GenerativeModel('gemini-pro-vision')

def get_response_gemini_pro_vision(input,image):
   
   if input!="":
      response = model.generate_content([input,image])
   else:
      response = model.generate_content(image)
      
   return response.text



st.set_page_config(page_title='Gemini AI Image Detector')
st.header("Google Gemini AI App")
input = st.text_input("Input:", key='input')

file_uploaded  = st.file_uploader("image ...", type=["jpg", "jpeg", "png"])
image = ""

col1, col2, col3 = st.columns(3)

if file_uploaded is not None:    
    image = Image.open(file_uploaded)
    with col2:
      st.image(image=image, caption="Upload image.")


submit = st.button("Tell me about the uploaded image?")
if submit:
    response = get_response_gemini_pro_vision(input, image)
    st.subheader("The details about the image is...")
    st.write(response)



