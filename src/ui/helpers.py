from typing import TypedDict
import streamlit as st
from utils.writing_samples import extract_writing_samples_from_github

class SessionState(TypedDict, total=False):
    original_blog: str
    translated_blog: str
    current_topic: str
    is_generating: bool
    writing_samples: list[str]


def init_session_state():
    """Initialize session state variables."""
    if 'original_blog' not in st.session_state:
        st.session_state.original_blog = None
    if 'translated_blog' not in st.session_state:
        st.session_state.translated_blog = None
    if 'current_topic' not in st.session_state:
        st.session_state.current_topic = ""
    if 'is_generating' not in st.session_state:
        st.session_state.is_generating = False
    if 'writing_samples' not in st.session_state:
        with st.spinner("Cargando ejemplos de escritura de GitHub..."):
            st.session_state.writing_samples = extract_writing_samples_from_github()

def set_generating_state(state):
    """Set the generating state in the session."""
    st.session_state.is_generating = state


