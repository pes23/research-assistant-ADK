import json, os

CACHE_PATH = "cache/parsed.json"

def save_cache(data: dict) -> str:
    os.makedirs("cache", exist_ok=True)
    with open(CACHE_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    return "Cache saved."

def load_cache() -> str:
    """Load parsed paper content from cache."""  
    if not os.path.exists(CACHE_PATH):
        return "No paper loaded. Please load a paper first using load_paper tool."
    with open(CACHE_PATH, "r", encoding="utf-8") as f:
        return json.dumps(json.load(f), ensure_ascii=False)
