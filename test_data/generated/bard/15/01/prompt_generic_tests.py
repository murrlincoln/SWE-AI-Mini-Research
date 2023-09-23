def function(a: str) -> str:
  """Capitalizes the first letter of each word in a string.

  Args:
    a: A string.

  Returns:
    A string with the first letter of each word capitalized.
  """

  words = a.split()
  capitalized_words = []
  for word in words:
    capitalized_words.append(word.capitalize())
  return " ".join(capitalized_words)
