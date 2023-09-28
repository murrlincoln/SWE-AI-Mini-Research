def function(a: str) -> str:
    words = a.split()
    if not words:
        return ''
    return words[0]
