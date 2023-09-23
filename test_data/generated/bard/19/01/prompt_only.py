def fibonacci(num: int) -> list:
  """Generates a Fibonacci sequence up to the given number.

  Args:
    num: The number of Fibonacci numbers to generate.

  Returns:
    A list of Fibonacci numbers, up to the given number.
  """

  if num < 0:
    raise ValueError("num must be a non-negative integer.")

  fibonacci_sequence = [0, 1]
  for i in range(2, num + 1):
    fibonacci_sequence.append(fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2])

  return fibonacci_sequence
