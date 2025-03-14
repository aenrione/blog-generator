#!/usr/bin/env python3
"""
Blog Generator CLI - Generates blog posts in your writing style and translates them.
"""

import sys
from dotenv import load_dotenv
from utils.general import setup_argparse, prompt_for_input
from utils.writing_samples import fetch_samples
from utils.llm import handle_origin_blog, handle_translation


def main(args=None):
    """Main function for the blog generator."""
    load_dotenv()

    parser = setup_argparse()
    args = parser.parse_args(args)
    args = prompt_for_input(args)

    samples = fetch_samples()
    if not samples:
        print("No writing samples found.")
        # return 1

    spanish_blog = handle_origin_blog(
        args.topic,
        samples,
        args.word_count,
        args.suggestions,
        args.model,
        args.output_dir,
        args.skip_download
    )

    if args.translate:
        handle_translation(
            spanish_blog,
            args.language,
            args.model,
            args.topic,
            args.output_dir
        )

    return 0


if __name__ == "__main__":
    sys.exit(main())

