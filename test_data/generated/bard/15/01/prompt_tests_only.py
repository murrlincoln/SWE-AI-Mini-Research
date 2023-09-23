def capitalize(text: str) -> str:
  """Capitalizes the first letter of each word in a string.

  Args:
    text: The string to capitalize.

  Returns:
    A string with the first letter of each word capitalized.
  """

  words = text.split()
  capitalized_words = [word.capitalize() for word in words]
  return ' '.join(capitalized_words)
