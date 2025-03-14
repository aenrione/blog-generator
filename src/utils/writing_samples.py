import os
import requests
import tempfile
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader

from config import GITHUB_SAMPLE_INFO, MAX_SAMPLES

def fetch_samples():
    """Fetch writing samples from GitHub."""
    print("Extrayendo ejemplos de escritura de GitHub...")
    samples = extract_writing_samples_from_github()

    if not samples:
        print("No se encontraron ejemplos de escritura. Verifica el repositorio.")
        return None

    print(f"Se extrajeron {len(samples)} ejemplos de escritura.")
    return samples



def get_github_content():
    """Get content from GitHub repository using the GitHub API."""
    repo = GITHUB_SAMPLE_INFO["repo"]
    path = GITHUB_SAMPLE_INFO["path"]
    url = f"https://api.github.com/repos/{repo}/{path}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching GitHub content: {response.status_code}")
        print(response.text)
        return []

def extract_writing_samples_from_github():
    """Extract writing samples directly from GitHub repository."""

    contents = get_github_content()

    if not contents:
        return []

    # Filter for markdown files
    md_files = [item for item in contents if item['name'].endswith('.md')]

    samples = []
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=100,
        separators=["\n## ", "\n### ", "\n#### ", "\n", " ", ""]
    )

    # Create temp directory for MD files
    with tempfile.TemporaryDirectory() as temp_dir:
        for file_info in md_files[:MAX_SAMPLES]:
            file_url = file_info['download_url']
            content = requests.get(file_url).text

            # Save MD file temporarily
            file_path = os.path.join(temp_dir, file_info['name'])
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)

            # Load the document
            loader = TextLoader(file_path, encoding='utf-8')
            documents = loader.load()

            # Split the document into chunks
            chunks = text_splitter.split_documents(documents)

            # Extract main content (excluding frontmatter)
            for chunk in chunks:
                text = chunk.page_content

                # Skip frontmatter
                if '---' in text[:20]:
                    parts = text.split('---', 2)
                    if len(parts) >= 3:
                        text = parts[2]

                # Clean and add to samples if it's substantial
                text = text.strip()
                if len(text) > 200:  # Only include substantial chunks
                    samples.append(text)

    return samples[:MAX_SAMPLES]
