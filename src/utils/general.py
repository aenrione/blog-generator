from pathlib import Path
import argparse
from pathlib import Path
from config import DEFAULT_GPT_MODEL, DEFAULT_WORD_COUNT

def save_file(content, filename, output_dir=None):
    """Save content to a file in the specified directory."""
    if output_dir:
        output_path = Path(output_dir)
        output_path.mkdir(exist_ok=True, parents=True)
        file_path = output_path / filename
    else:
        file_path = Path(filename)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

    return file_path


def create_filename(topic, lang_code):
    """Create a standardized filename for the output."""
    sanitized_topic = topic.replace(' ', '_')
    return f"{sanitized_topic}_blog_{lang_code}.md"


def setup_argparse():
    """Configure command line argument parsing."""
    parser = argparse.ArgumentParser(
        description="Generate blog posts in your writing style and translate them.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument("topic", nargs="?", help="Blog topic")
    parser.add_argument(
        "-w", "--word-count",
        type=int,
        default=DEFAULT_WORD_COUNT,
        help="Target word count for the blog post"
    )
    parser.add_argument(
        "-m", "--model",
        default=DEFAULT_GPT_MODEL,
        help="GPT model to use for generation"
    )
    parser.add_argument(
        "-s", "--suggestions",
        help="Additional suggestions for content"
    )
    parser.add_argument(
        "-t", "--translate",
        action="store_true",
        help="Enable translation"
    )
    parser.add_argument(
        "-l", "--language",
        default="English",
        help="Target language for translation"
    )
    parser.add_argument(
        "-o", "--output-dir",
        help="Directory to save output files"
    )
    parser.add_argument(
        "--skip-download",
        action="store_true",
        help="Skip original blog output (only generate translation)"
    )

    return parser


def prompt_for_input(args):
    """Prompt for missing arguments interactively."""
    if not args.topic:
        args.topic = input("Ingresa un tema para el blog (en español): ")
        word_count_input = input(
            f"Ingresa el número de palabras deseado (default {DEFAULT_WORD_COUNT}): "
        )
        if word_count_input.isdigit():
            args.word_count = int(word_count_input)
    return args


