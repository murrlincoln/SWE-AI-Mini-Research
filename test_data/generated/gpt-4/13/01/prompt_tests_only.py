def is_palindrome(text: str) -> bool:
    cleaned_text = ''.join(e for e in text if e.isalnum()).lower()  # Remove non-alphanumeric and convert to lowercase
    return cleaned_text == cleaned_text[::-1]
