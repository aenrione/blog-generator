import streamlit as st
from config import DEFAULT_WORD_COUNT, LANGUAGE_OPTIONS, MODELS_OPTIONS, DEFAULT_GPT_MODEL, DEFAULT_TRANSLATION_LANGUAGE

def input_section():
    """Render the input form elements and return their values."""
    topic = st.text_input("Tema del Blog")
    suggestions = st.text_area("Sugerencias para el Blog", height=100)
    word_count = st.number_input(
        "Número de Palabras",
        min_value=100,
        value=DEFAULT_WORD_COUNT,
        step=100
    )

    gpt_model = DEFAULT_GPT_MODEL
    gpt_model = st.selectbox(
        "Modelo de Lenguaje",
        options=list(MODELS_OPTIONS.keys()),
        index=0
    )

    translate = st.checkbox("Traducir a otro idioma", value=True)

    target_language = DEFAULT_TRANSLATION_LANGUAGE
    if translate:
        target_language = st.selectbox(
            "Idioma de traducción",
            options=list(LANGUAGE_OPTIONS.keys()),
            index=0
        )

    return topic, suggestions, word_count, gpt_model, translate, target_language

def create_generate_button():
    """Create and return the generate button."""
    return st.button(
        "Generar Blog",
        disabled=st.session_state.is_generating,
        key="generate_button"
    )

def display_download_buttons(language):
    """Display download buttons for generated content."""
    if st.session_state.original_blog:
        st.download_button(
            label="Descargar en Español (Markdown)",
            data=st.session_state.original_blog,
            file_name=f"{st.session_state.current_topic.replace(' ', '_')}_blog_es.md",
            mime="text/markdown",
            key="download_spanish"
        )

    if st.session_state.translated_blog:
        language_code = language.lower()[:2]  # Get language code for filename
        st.download_button(
            label=f"Descargar en {language} (Markdown)",
            data=st.session_state.translated_blog,
            file_name=f"{st.session_state.current_topic.replace(' ', '_')}_blog_{language_code}.md",
            mime="text/markdown",
            key="download_translated"
        )

