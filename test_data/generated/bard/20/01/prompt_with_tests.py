def fizzbuzz(num: int) -> str:
  """Prints the numbers 1 to 100, but printing 'Fizz' for multiples of 3, 'Buzz' for multiples of 5, and 'FizzBuzz' for multiples of both 3 and 5.

  Args:
    num: The number to print.

  Returns:
    A string containing the number, or 'Fizz', 'Buzz', or 'FizzBuzz' if the number is a multiple of 3, 5, or both, respectively.
  """

  if num % 3 == 0 and num % 5 == 0:
    return 'FizzBuzz'
  elif num % 3 == 0:
    return 'Fizz'
  elif num % 5 == 0:
    return 'Buzz'
  else:
    return str(num)

