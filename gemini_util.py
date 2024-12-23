import os
import json
import streamlit as st
import google.generativeai as genai


gemini_api_key = st.secrets["api_key"]
os.environ["GEMINI_API_KEY"] = gemini_api_key


genai.configure(api_key=gemini_api_key)


def load_model():
    gemini_model = genai.GenerativeModel("gemini-1.5-flash")
    return gemini_model

def load_vision_model(prompt, image):
    vision_model = genai.GenerativeModel("gemini-1.5-flash")
    response = vision_model.generate_content([prompt, image])
    return response.text

def load_embed_model(input_text):
    embedding = genai.embed_content("models/text-embedding-004",
                                          input_text,
                                          "retrieval_document")
    embedding_list = embedding["embedding"]
    return embedding_list

def gemini_response(user_prompt):
    gemini_model = genai.GenerativeModel("gemini-1.5-flash")
    response = gemini_model.generate_content(user_prompt)
    result = response.text
    return result
