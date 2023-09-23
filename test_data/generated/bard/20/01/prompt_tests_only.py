def fizzbuzz(num: int) -> str:
  """Returns 'Fizz' if num is divisible by 3, 'Buzz' if num is divisible by 5, and 'FizzBuzz' if num is divisible by both 3 and 5. Otherwise, returns str(num)."""
  if num % 3 == 0 and num % 5 == 0:
    return 'FizzBuzz'
  elif num % 3 == 0:
    return 'Fizz'
  elif num % 5 == 0:
    return 'Buzz'
  else:
    return str(num)
