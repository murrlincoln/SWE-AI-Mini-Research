def reverse_string(text: str) -> str:
  """Reverses a string.

  Args:
    text: The string to reverse.

  Returns:
    The reversed string.
  """

  reversed_string = ""
  for i in range(len(text) - 1, -1, -1):
    reversed_string += text[i]
  return reversed_string
