def bubble_sort(arr: List[int]) -> List[int]:
  """Sorts a list of integers in ascending order using the bubble sort algorithm.

  Args:
    arr: A list of integers.

  Returns:
    A list of integers sorted in ascending order.
  """

  for i in range(len(arr) - 1):
    for j in range(len(arr) - i - 1):
      if arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]

  return arr
