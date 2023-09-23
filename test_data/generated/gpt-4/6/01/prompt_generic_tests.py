def function(a: str) -> bool:
    return '@' in a and '.' in a.split('@')[1]
