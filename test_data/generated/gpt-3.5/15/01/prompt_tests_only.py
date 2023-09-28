def capitalize(text: str) -> str:
    if not text:
        return text

    words = text.split()
    capitalized_words = [word.capitalize() for word in words]
    return ' '.join(capitalized_words)
