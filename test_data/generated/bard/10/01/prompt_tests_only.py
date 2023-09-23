def factorial_recursive_2(n: int) -> int:
  """Calculates the factorial of a number recursively.

  Args:
    n: The number to calculate the factorial of.

  Returns:
    The factorial of n.
  """

  if n == 0 or n == 1:
    return 1
  else:
    return n * factorial_recursive_2(n - 1)
