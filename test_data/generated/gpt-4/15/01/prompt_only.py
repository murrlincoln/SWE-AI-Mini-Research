def capitalize(text: str) -> str:
    return ' '.join(word.capitalize() for word in text.split())
