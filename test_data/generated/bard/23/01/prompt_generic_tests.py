def function(a: str, b: int) -> str:
  result = ''
  for i in range(len(a)):
    if i % b == 0:
      result += a[i]
  return result
