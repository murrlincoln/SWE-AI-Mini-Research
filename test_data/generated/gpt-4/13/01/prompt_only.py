def is_palindrome(text: str) -> bool:
    cleaned_text = ''.join(char for char in text if char.isalnum()).lower()
    return cleaned_text == cleaned_text[::-1]
