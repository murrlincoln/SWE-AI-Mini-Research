def test_negative():
  num = -5
  assert fibonacci(num) == []

def fibonacci(num):
  if num <= 0:
    return []
  elif num == 1:
    return [0, 1]
  else:
    return fibbonacci_seq(num)

def fibbonacci_seq(num):
  a = 0
  b = 1
  output = [a, b]
  for i in range(2, num):
    c = a + b
    a = b
    b = c
    output.append(c)
  return output