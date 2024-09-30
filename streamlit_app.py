import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

genai.configure(api_key = "AIzaSyDw0SnHIWq68Z4_-31GyIvbZhsl_Pbfmjc")
model = genai.GenerativeModel("gemini-1.5-flash")

def get_gemini_response(input_text, image_data, prompt):
    response = model.generate_content([input_text, image_data[0], prompt])
    # response = model.generate_content('Tell me a story about a magic backpack')
    return response.text

def input_image_details(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = [
            {
                "mime_type" : uploaded_file.type,
                "data" : bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("FILE NOT FOUND!!")

st.set_page_config(page_title="Solution Provider + Translator")
st.sidebar.header("Sidebar_Placeholder")
st.sidebar.write("Made by Vi ")
st.header("Solun Tran")
st.subheader("Provides Solutions and Translations")
input_prompt = st.text_input("What do you want me to do?",key="input")
uploaded_file = st.file_uploader("Choose an image",type=["jpg","jpeg","png"])
image_var = ""
if uploaded_file is not None:
    image_var= Image.open(uploaded_file)
    st.image(image_var,caption="Uploaded Image",use_column_width=True)

sumbit_but = st.button("Sumbit Image")

ai_prompt = """
You are a smart mathematisian and calculator . I will give you an image and you should solve the given question and give it to me in
mathematical steps
You are also a translator and i will upload an image in a particular language and you will give me the output in english
 """

if sumbit_but:
    image_data = input_image_details(uploaded_file)
    response = get_gemini_response(ai_prompt,image_data,input_prompt)
    st.subheader("Here's what you need to know.")
    st.write(response)
