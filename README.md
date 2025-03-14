# Blog Generator with LLM's

This is a simple blog generator using LLM's. The idea is to facilitate a topic generation for a blog post while using writing samples from a specific author in order to make it sound more like that author.

The model currently used is `gpt-3.5-turbo`|`gpt-4` from OpenAI.

The idea is to help people who have a hard time starting a blog post or need some inspiration to write about a specific topic. The format is in `markdown` so it can be easily imported to a blog platform like [`Hugo`](https://gohugo.io/).



https://github.com/user-attachments/assets/f4e72bed-786e-4d45-98a6-7897d5dbb99a


## Requirements
- Python 3.8+
- OpenAI API key

## Features
- Generate a blog post based on a prompt.
- Download the generated blog post as a markdown file.
- Web app to facilitate the usage.
- Translate the generated blog post to another language and download it as a markdown file.

## How to use

1. Install the requirements:
A virtual environment is recommended.
```bash
python3 -m venv venv
source venv/bin/activate # Linux or MacOS - For Windows use venv\Scripts\activate
pip install -r requirements.txt
```

2. Set your OpenAI API key:
```bash
cp .env.example .env
vi .env
```

3. Configure `src/config.py` with the desired parameters or leave the default values.

4. Run either the CLI or the web app:
```bash
python3 src/blog_generator.py # CLI
# or
streamlit run src/app.py # Web app
```
## Configuration
The `src/config.py` file contains the following parameters:

- `MODELS_OPTIONS`: Available models to use. Could be extended to other models.
- `DEFAULT_GPT_MODEL`: Default model to use.
- `DEFAULT_WORD_COUNT`: Default word count for the generated blog post.
- `MAX_SAMPLES`: Maximum number of writing samples to use.
- `GITHUB_SAMPLE_INFO`: Information about the writing samples. Currently it retrieves them from a GitHub repository.
- `DEFAULT_TRANSLATION_LANGUAGE`: Default language to translate the generated blog post.
- `LANGUAGE_OPTIONS`: Available languages to translate the generated blog post.
