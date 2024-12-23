import os
import json

import google.generativeai as genai

working_dir = os.path.dirname(os.path.abspath(__file__))
config_file_path = f"{working_dir}/config.json"
config_data = json.load(open(config_file_path))

GOOGLE_API_KEY = config_data["GOOGLE_API_KEY"]

genai.configure(api_key=GOOGLE_API_KEY)


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