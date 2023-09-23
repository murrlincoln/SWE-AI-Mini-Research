def fibonacci(num: int) -> list:
  """Returns a list of the Fibonacci numbers up to and including `num`.

  Args:
    num: An integer.

  Returns:
    A list of integers, representing the Fibonacci sequence up to and including `num`.
  """

  if num < 0:
    raise ValueError("Input number must be non-negative.")

  # The first two Fibonacci numbers are 0 and 1.
  fibonacci_sequence = [0, 1]

  # Iterate from 2 to `num`, adding the previous two numbers in the sequence to
  # get the next number.
  for i in range(2, num + 1):
    fibonacci_sequence.append(fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2])

  return fibonacci_sequence

