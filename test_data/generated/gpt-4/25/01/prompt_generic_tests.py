def function(a: str, b: str) -> str:
    result = ''
    for char in b:
        if char in a:
            result += char
    return result
