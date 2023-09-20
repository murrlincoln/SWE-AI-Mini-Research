def test_4():
  input = -2
  assert function(input) == 1

def function(x):
  if x < 0:
    return 1
  prod = 1
  for i in range(1, x+1):
    prod *= i
  return prod