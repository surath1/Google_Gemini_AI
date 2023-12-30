### LLM Google Gemini AI 

- API Key - https://makersuite.google.com/app/apikey

- Tutorials - https://ai.google.dev/tutorials/python_quickstart

- colab - https://colab.research.google.com/github/google/generative-ai-docs/blob/main/site/en/tutorials/python_quickstart.ipynb


### project setup
```bash
!pip install streamlit
!pip install google-generativeai
!pip install python-dotenv

conda create -p aienv python==3.11.4
conda activate aienv/
pip install -r requirements.txt

# GOOGLE_API_KEY=""
```

###  API verification 
```bash
import os
os.environ["GOOGLE_API_KEY"] = ""
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)

## python main.py
#  models/gemini-pro
#  models/gemini-pro-vision

```

### generate text
```bash
model = genai.GenerativeModel('gemini-pro')
response = model.generate_content("What is the GDP of USA?")
print(response.text)
# As of 2023, the GDP of the United States is estimated to be around $25.3 trillion, making it the largest economy in the world.
print(response.prompt_feedback)
```

### generate text chunk
```bash
%time
response = model.generate_content("Write a poem about elephant maximum 100 words?", stream=True)
for chunk in response:
  print(chunk.text)
  print("_"*80)


```

### streamlit gemini pro q&a app 
```bash
model = genai.GenerativeModel('gemini-pro')
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


# streamlit run main.py
```

### streamlit gemini pro vision app 
```bash
model = genai.GenerativeModel('gemini-pro-vision')
def get_response_gemini_pro_vision(input, image):
    if input is not empty:
        response = model.generate_content([input, image])   
    else:
        response = model.generate_content(image)
    return response.text

```