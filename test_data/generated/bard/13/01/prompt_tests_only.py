def is_palindrome(text: str) -> bool:
  """Returns True if the given text is a palindrome, False otherwise."""
  text = text.lower()
  return text == text[::-1]
