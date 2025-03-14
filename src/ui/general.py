import streamlit as st

def display_header():
    """Display the app header and description."""
    st.title("Generador de Blogs")
    st.write("Esta aplicación genera blogs en español en tu estilo y los traduce.")
    if st.button("🔗 Código fuente"):
        st.write("https://github.com/aenrione/blog-generator")

    if st.session_state.writing_samples is None or st.session_state.writing_samples == []:
        st.markdown("<span style='color:red'>Nota: No cuentas con ejemplos de escritura. Revisa tu configuracion.</span>", unsafe_allow_html=True)


