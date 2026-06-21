def clean_text(text: str) -> str:
    """Basic text cleaning."""
    if text is None:
        return ""
    return " ".join(str(text).strip().lower().split())
