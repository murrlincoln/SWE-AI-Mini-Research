def is_palindrome(text: str) -> bool:
    # Remove spaces and convert to lowercase for case-insensitive comparison
    text = text.replace(" ", "").lower()
    
    # Check if the string is equal to its reverse
    return text == text[::-1]
