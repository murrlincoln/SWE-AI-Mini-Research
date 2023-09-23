def fibonacci(num: int) -> list:
  """Returns a list of the first `num` Fibonacci numbers.

  Args:
    num: The number of Fibonacci numbers to return.

  Returns:
    A list of the first `num` Fibonacci numbers.
  """

  if num < 0:
    raise ValueError("num must be non-negative")

  fib_list = [0] * (num + 1)
  fib_list[0] = 0
  fib_list[1] = 1

  for i in range(2, num + 1):
    fib_list[i] = fib_list[i - 1] + fib_list[i - 2]

  return fib_list
