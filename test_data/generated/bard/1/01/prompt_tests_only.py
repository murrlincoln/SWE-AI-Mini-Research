def reverse_vowels(s: str) -> str:
  vowels = set('aeiou')
  vowels_idx = [i for i, c in enumerate(s) if c in vowels]
  vowels_idx.reverse()
  vowels_reversed = [s[i] for i in vowels_idx]
  for i, idx in enumerate(vowels_idx):
    s = s[:idx] + vowels_reversed[i] + s[idx + 1:]
  return s
