from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from config import DEFAULT_GPT_MODEL
from templates import BLOG_TEMPLATE, TRANLATION_TEMPLATE
from .general import save_file, create_filename

def create_template(writing_samples):
    """Create a personalized template with writing examples."""
    samples_text = "".join(writing_samples)
    return BLOG_TEMPLATE, samples_text


def create_llm_chain(template, model=DEFAULT_GPT_MODEL, temp=0.7, variables=None):
    """Create a language model chain with the given template."""
    if variables is None:
        variables = []

    llm = ChatOpenAI(model=model, temperature=temp)
    prompt = PromptTemplate(input_variables=variables, template=template)
    return LLMChain(llm=llm, prompt=prompt)


def generate_blog(topic, samples, word_count, suggestions=None, model=DEFAULT_GPT_MODEL):
    """Generate a blog post using the personalized template."""
    template, samples_text = create_template(samples)
    chain = create_llm_chain(
        template,
        model=model,
        variables=["writing_examples", "topic", "word_count", "suggestions"]
    )

    return chain.run(
        writing_examples=samples_text,
        topic=topic,
        word_count=word_count,
        suggestions=suggestions or ""
    )


def translate_content(content, target_language, model=DEFAULT_GPT_MODEL):
    """Translate content to the target language."""
    template = TRANLATION_TEMPLATE.format(target_language=target_language)
    chain = create_llm_chain(template, model=model, temp=0.3, variables=["spanish_content"])
    return chain.run(spanish_content=content)




def handle_origin_blog(topic, samples, word_count, suggestions, model, output_dir, skip_download=False):
    """Generate and optionally save the blog post."""
    print("\nGenerando artículo de blog en español...\n")
    generated_blog = generate_blog(topic, samples, word_count, suggestions, model)

    if not skip_download:
        filename = create_filename(topic, "es")
        file_path = save_file(generated_blog, filename, output_dir)
        print(f"\nBlog en español guardado como {file_path}")

    return generated_blog


def handle_translation(content, language, model, topic, output_dir):
    """Translate and save the blog post to the target language."""
    print(f"\nTraduciendo a {language}...\n")
    translated_blog = translate_content(content, language, model)

    filename = create_filename(topic, language)

    file_path = save_file(translated_blog, filename, output_dir)
    print(f"\nBlog traducido guardado como {file_path}")

