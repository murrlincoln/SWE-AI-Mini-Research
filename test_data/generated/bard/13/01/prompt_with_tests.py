def is_palindrome(text: str) -> bool:
  """Returns True if text is a palindrome, False otherwise.

  Args:
    text: A string.

  Returns:
    A bool.
  """

  text = text.lower()
  return text == text[::-1]
