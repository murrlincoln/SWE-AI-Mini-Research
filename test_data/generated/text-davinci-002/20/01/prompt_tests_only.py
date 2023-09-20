def test_num():
  num = 7
  assert fizzbuzz(num) == num

def fizzbuzz(num):
  if num % 15 == 0:
    return "FizzBuzz"
  if num % 3 == 0:
    return "Fizz"
  if num % 5 == 0:
    return "Buzz"
  return num