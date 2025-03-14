import streamlit as st
from utils.llm import translate_content, generate_blog
from config import  LANGUAGE_OPTIONS
from .helpers import set_generating_state

def generate_translation(content, language, model):
    """Generate the translation and update session state."""
    language_display = LANGUAGE_OPTIONS.get(language, "inglés")
    with st.spinner(f"Traduciendo al {language_display}..."):
        translated_blog = translate_content(content, language, model)
        st.session_state.translated_blog = translated_blog

        st.subheader(f"Blog en {language}")
        st.markdown(translated_blog)

def generate_spanish_blog(topic, suggestions, word_count, model):
    """Generate the Spanish blog and update session state."""
    with st.spinner("Generando blog en español..."):
        original_blog = generate_blog(
            topic,
            st.session_state.writing_samples,
            word_count,
            suggestions,
            model
        )
        st.session_state.original_blog = original_blog
        st.session_state.current_topic = topic

        st.subheader("Blog en Español")
        st.markdown(original_blog)

    return original_blog


def handle_generation(topic, suggestions, word_count, model, translate, language):
    """Handle the blog generation flow."""
    if not topic:
        st.error("Por favor ingresa un tema!")
        return

    try:
        set_generating_state(True)

        original_blog = generate_spanish_blog(topic, suggestions, word_count, model)

        if translate:
            generate_translation(original_blog, language, model)
        else:
            st.session_state.translated_blog = None

    finally:
        set_generating_state(False)

