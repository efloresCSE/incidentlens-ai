def normalize_message(message: str) -> str:
    """Normalize casing and whitespace in a log message."""
    return " ".join(message.lower().split())


def classify_severity(message: str) -> str:
    """Classify a message as an error or other."""
    normalized = normalize_message(message)

    if "error" in normalized:
        return "error"

    return "other"
