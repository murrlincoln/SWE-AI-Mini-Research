- Input: -1.5
  Expected Output: ValueError: Cannot calculate the factorial of a negative number

def factorial(n):
  if n < 0:
    raise ValueError("Cannot calculate the factorial of a negative number")
  elif n == 0:
    return 1
  else:
    return n * factorial(n - 1)