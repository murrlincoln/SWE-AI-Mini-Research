def count_vowels(text: str) -> int:
  """Counts the number of vowels in a string.

  Args:
    text: A string.

  Returns:
    The number of vowels in the string.
  """

  vowels = set("aeiou")
  count = 0
  for char in text:
    if char in vowels:
      count += 1
  return count
