def capitalize(text: str) -> str:
  """Capitalizes words in string.

  Args:
    text: A string.

  Returns:
    A string with capitalized words.
  """

  words = text.split()
  capitalized_words = [word.capitalize() for word in words]
  return " ".join(capitalized_words)
