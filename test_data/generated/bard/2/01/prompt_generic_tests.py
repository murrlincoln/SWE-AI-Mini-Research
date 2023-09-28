def function(a: List[int], b: List[int]) -> List[int]:
  """Merges two sorted lists into a single sorted list.

  Args:
    a: A sorted list of integers.
    b: A sorted list of integers.

  Returns:
    A sorted list containing all elements of `a` and `b`.
  """

  merged_list = []
  i = 0
  j = 0
  while i < len(a) and j < len(b):
    if a[i] < b[j]:
      merged_list.append(a[i])
      i += 1
    else:
      merged_list.append(b[j])
      j += 1

  # Add the remaining elements of the longer list.
  if i < len(a):
    merged_list.extend(a[i:])
  elif j < len(b):
    merged_list.extend(b[j:])

  return merged_list
