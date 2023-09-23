def fizzbuzz(num: int) -> str:
  """FizzBuzz function.

  Args:
    num: The number to fizzbuzz.

  Returns:
    A string containing "Fizz" if the number is divisible by 3, "Buzz" if the
    number is divisible by 5, and the number itself otherwise.
  """

  if num % 3 == 0 and num % 5 == 0:
    return "FizzBuzz"
  elif num % 3 == 0:
    return "Fizz"
  elif num % 5 == 0:
    return "Buzz"
  else:
    return str(num)
