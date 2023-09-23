def is_palindrome(text: str) -> bool:
  """
  Checks if a string is a palindrome.

  Args:
    text: The string to check.

  Returns:
    True if the string is a palindrome, False otherwise.
  """

  text = text.lower()
  reversed_text = text[::-1]
  return text == reversed_text
