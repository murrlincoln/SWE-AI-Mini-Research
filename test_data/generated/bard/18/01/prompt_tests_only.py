def factorial(num: int) -> int:
  """Calculates the factorial of a number.

  Args:
    num: The number to calculate the factorial of.

  Returns:
    The factorial of the number.
  """

  if num < 0:
    raise ValueError("num must be a non-negative integer.")
  elif num == 0:
    return 1
  else:
    return num * factorial(num - 1)
