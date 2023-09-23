def reverse_string(text: str) -> str:
  """Reverses the order of the characters in a string.

  Args:
    text: The string to reverse.

  Returns:
    A string with the characters in the reverse order.
  """

  reversed_text = ''
  for i in range(len(text) - 1, -1, -1):
    reversed_text += text[i]
  return reversed_text
