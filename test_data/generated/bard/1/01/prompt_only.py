def reverse_vowels(s: str) -> str:
  """Reverses the vowels in a given string.

  Args:
    s: A string.

  Returns:
    A string with the vowels reversed.
  """

  vowels = set("aeiou")
  vowels_idx = [i for i, c in enumerate(s) if c in vowels]
  vowels_reversed = vowels_idx[::-1]
  vowels_dict = dict(zip(vowels_idx, vowels_reversed))
  result = ""
  for i, c in enumerate(s):
    if c in vowels:
      result += s[vowels_dict[i]]
    else:
      result += c
  return result
