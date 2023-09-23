def function(a: str) -> str:
  result = ''
  for i in range(len(a)):
    if a[i] not in result:
      result += a[i]
  return result
