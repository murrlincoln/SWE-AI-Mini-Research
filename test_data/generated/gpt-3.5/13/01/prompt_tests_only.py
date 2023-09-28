def is_palindrome(text: str) -> bool:
    # Remove spaces and convert to lowercase for case-insensitive comparison
    text = text.replace(" ", "").lower()
    
    # Check if the text is equal to its reverse
    return text == text[::-1]
