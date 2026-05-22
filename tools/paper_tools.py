from tools.pdf_tools import extract_pdf
from tools.chunk_tools import chunk_paper
from tools.cache_tools import save_cache

def load_paper(path: str) -> str:
    """Load and parse a PDF paper from the given path, then cache it for analysis."""
    try:
        text = extract_pdf(path)
        sections = chunk_paper(text)
        save_cache(sections)
        loaded = [k for k, v in sections.items() if v]
        return f"Paper loaded successfully. Sections found: {', '.join(loaded)}"
    except FileNotFoundError:
        return f"File not found: {path}"
    except Exception as e:
        return f"Error loading paper: {e}"
