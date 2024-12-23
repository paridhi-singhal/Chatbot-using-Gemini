import streamlit as st
import os
from streamlit_option_menu import option_menu
from gemini_util import (load_model, load_vision_model, load_embed_model, gemini_response)
from PIL import Image

st.set_page_config(
    page_title="Gemini AI",
    page_icon="🧠",
    layout="centered"
)

with st.sidebar:

    selected = option_menu("Gemini AI",
                           ["ChatBot",
                            "Image Captioning",
                            "Embed Text",
                            "Ask Me Anything"],
                            default_index=0)

def translate_role_for_streamlit(user_role):
    if user_role =='model':
        return "assistant"
    else:
        return user_role

if selected == "ChatBot":
    model = load_model()

    if "chat_session" not in st.session_state:
        st.session_state.chat_session = model.start_chat(history=[])

    st.title(" 🤖 Chatbot")

    for message in st.session_state.chat_session.history:
        with st.chat_message(translate_role_for_streamlit(message.role)):
            st.markdown(message.parts[0].text)

    user_prompt = st.chat_input("Ask gemini..")

    if user_prompt:
        st.chat_message("user").markdown(user_prompt)

        gemini_response = st.session_state.chat_session.send_message(user_prompt)

        with st.chat_message("assistant"):
            st.markdown(gemini_response.text)

if selected == "Image Captioning":
    st.title(" 📷 Snap Narrate")

    uploaded_image = st.file_uploader("Upload an image.." , type=["jpg, jpeg", "png"])

    if st.button("Generate Caption"):
        image = Image.open(uploaded_image)

        col1, col2 = st.columns(2)

        with col1:
            resized_image = image.resize((800,500))
            st.image(resized_image)

        default_prompt = "write a short caption for this image"
        caption = load_vision_model(default_prompt,image)

        with col2:
            st.info(caption)

if selected == "Embed Text":
    st.title("🔡 Embed Text")
    input_text = st.text_area(label="", placeholder="Enter the text to get the embeddings")
    if st.button("get Embeddings"):
        response = load_embed_model(input_text)
        st.markdown(response)


if selected == "Ask Me Anything":
    st.title("❔ Ask me a Question")
    user_prompt = st.text_area(label="", placeholder="Ask me anything..")
    if st.button("Get an answer"):
        response = gemini_response(user_prompt)
        st.markdown(response)
