def function(a: str) -> bool:
    cleaned_string = ''.join(e for e in a if e.isalnum()).lower()
    return cleaned_string == cleaned_string[::-1]
