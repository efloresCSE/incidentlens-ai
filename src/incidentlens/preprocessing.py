def normalize_message(message: str) -> str:
    """Normalize casing and whitespace in a log message."""
    return " ".join(message.lower().split())
