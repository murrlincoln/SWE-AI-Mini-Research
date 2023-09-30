def fibonacci(n: int) -> List[int]:
  fib = [0, 1]
  if n < 2:
    return fib[:n+1]
  else:
    for i in range(2, n+1):
      fib.append(fib[i-1] + fib[i-2])
    return fib
