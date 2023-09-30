def fibonacci(num: int) -> List[int]:
  result = [0]
  a, b = 0, 1
  for i in range(1, num+1):
    result.append(b)
    a, b = b, a + b
  return result
