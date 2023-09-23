def bubble_sort(arr: List[int]) -> List[int]:
  """
  Sorts an array using the bubble sort algorithm.

  Args:
    arr: A list of integers.

  Returns:
    A sorted list of integers.
  """

  swapped = True
  n = len(arr)
  while swapped:
    swapped = False
    for i in range(n - 1):
      if arr[i] > arr[i + 1]:
        arr[i], arr[i + 1] = arr[i + 1], arr[i]
        swapped = True
  return arr
