import streamlit as st
from googletrans import Translator

st.set_page_config(page_title="Language Translator", layout="centered")

st.title("🌍 Language Translation Tool")

translator = Translator()

text = st.text_area("Enter text to translate")

languages = {
    "English": "en",
    "Hindi": "hi",
    "Telugu": "te",
    "Tamil": "ta",
    "French": "fr",
    "German": "de",
    "Spanish": "es"
}

source_lang = st.selectbox("Source Language", languages.keys())
target_lang = st.selectbox("Target Language", languages.keys())

if st.button("Translate"):
    if text:
        translated = translator.translate(
            text,
            src=languages[source_lang],
            dest=languages[target_lang]
        )
        st.success("Translated Text:")
        st.write(translated.text)
    else:
        st.warning("Please enter text")
