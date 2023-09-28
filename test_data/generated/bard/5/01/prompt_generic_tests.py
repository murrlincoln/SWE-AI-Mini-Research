def function(a: str, b: str) -> int:
  count = 0
  for i in range(len(a)):
    if a[i] == b:
      count += 1
  return count
