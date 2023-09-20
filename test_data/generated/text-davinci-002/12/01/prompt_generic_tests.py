def test_4():
  input = ['key']
  assert function(input) == 0

def test_5():
  input = {'value': 'key'}
  assert function(input) == 0

def test_6():
  input = True
  assert function(input) == 0

def test_7():
  input = False
  assert function(input) == 0

def test_8():
  input = 1
  assert function(input) == 0

def test_9():
  input = 0
  assert function(input) == 0

def test_10():
  input = ' '
  assert function(input) == 0
def function(x):
  if isinstance(x, str):
    return len(x)
  else:
    return 0