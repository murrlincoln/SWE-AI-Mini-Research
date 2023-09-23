def bubble_sort(arr: List[int]) -> List[int]:
  """Sorts an array using the bubble sort algorithm.

  Args:
    arr: A list of integers to be sorted.

  Returns:
    A sorted list of integers.
  """

  swapped = True
  while swapped:
    swapped = False
    for i in range(len(arr) - 1):
      if arr[i] > arr[i + 1]:
        arr[i], arr[i + 1] = arr[i + 1], arr[i]
        swapped = True

  return arr

