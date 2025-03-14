from ui.helpers import init_session_state
from ui.general import display_header
from ui.form import input_section, create_generate_button, display_download_buttons
from ui.llm_elements import  handle_generation


def main():
    """Main application function."""
    init_session_state()
    display_header()

    topic, suggestions, word_count, model, translate, language = input_section()

    generate_button = create_generate_button()

    if generate_button:
        handle_generation(topic, suggestions, word_count, model, translate, language)

    display_download_buttons(language)

if __name__ == "__main__":
    main()
