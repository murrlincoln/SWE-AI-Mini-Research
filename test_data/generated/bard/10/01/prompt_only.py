def factorial_recursive_2(n: int) -> int:
  """Calculates the factorial of a given number using recursion.

  Args:
    n: The number to calculate the factorial of.

  Returns:
    The factorial of n.
  """

  if n == 0:
    return 1
  else:
    return n * factorial_recursive_2(n - 1)
