def fizzbuzz(a: int) -> str:
  if a % 15 == 0:
    return 'FizzBuzz'
  elif a % 3 == 0:
    return 'Fizz'
  elif a % 5 == 0:
    return 'Buzz'
