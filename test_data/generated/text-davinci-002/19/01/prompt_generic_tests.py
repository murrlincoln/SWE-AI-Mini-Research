def test_4():
  input = 9
  assert function(input) == [0, 1, 1, 2, 3, 5, 8, 13, 21]

def function(input):
  if input == 0:
    return [0]
  elif input == 1:
    return [0, 1]
  else:
    nums = function(input - 1)
    nums.append(nums[-2] + nums[-1])
    return nums