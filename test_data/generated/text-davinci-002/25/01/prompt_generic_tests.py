assert function('bc', 'abc') == None

def function(str1, str2):
  """
  Returns the longest common matched substring between str1 and str2. If no substring is found, returns None.
  """
  for i in range(min(len(str1), len(str2))):
    if str1[i] != str2[i]:
      return str1[:i]
  return min(str1, str2)