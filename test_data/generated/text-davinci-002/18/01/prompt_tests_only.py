def test_minus():
  num = -1
  assert factorial(num) == 1

def test_string():
  num = 'string'
  assert factorial(num) == 1

def factorial(num):
 if num < 0:
  return 1
 elif num == 0 or num == 1:
  return 1
 else:
  return num * factorial(num - 1)