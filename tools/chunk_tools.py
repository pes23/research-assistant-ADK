import re

def chunk_paper(text: str) -> dict:
    lower = text.lower()
    patterns = {
        "abstract":     r"abstract(.*?)(introduction|1\s+introduction)",
        "introduction": r"(introduction|1\s+introduction)(.*?)(method|model architecture|approach|3)",
        "method":       r"(method|model architecture|approach)(.*?)(experiment|results|evaluation|4)",
        "experiment":   r"(experiment|results|evaluation)(.*)",
        "conclusion":   r"(conclusion|discussion)(.*?)(future work|references|acknowledgment|$)"
    }
    return {
        key: re.search(p, lower, re.DOTALL).group(0)[:6000]
        if re.search(p, lower, re.DOTALL) else ""
        for key, p in patterns.items()
    }
