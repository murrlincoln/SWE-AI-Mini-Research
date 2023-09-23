def function(a: str) -> str:
    return ' '.join(word.capitalize() for word in a.split())
