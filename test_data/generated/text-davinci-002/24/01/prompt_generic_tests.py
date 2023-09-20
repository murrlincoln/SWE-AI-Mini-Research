def function(s):
  if len(s) % 2 == 1 and s[: (len(s)-1) // 2] == s[((len(s)-1) // 2) + 1:]:
    return s[(len(s)-1) // 2]
  elif s[: len(s) // 2] == s[len(s) // 2 + 1:]:
    return s[: len(s) // 2]
  else:
    return None