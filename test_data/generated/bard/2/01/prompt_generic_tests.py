def function(a: List[int]) -> List[int]:
  """Reverses a list in place.

  Args:
    a: A list of integers.

  Returns:
    A reversed list of integers.
  """

  left = 0
  right = len(a) - 1
  while left < right:
    a[left], a[right] = a[right], a[left]
    left += 1
    right -= 1
  return a
