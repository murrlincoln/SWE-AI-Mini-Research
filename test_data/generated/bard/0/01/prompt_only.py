def sort_even_numbers(arr: List[int]) -> List[int]:
  """Sorts the even numbers in the given array in ascending order while leaving the odd numbers in their original positions.

  Args:
    arr: A list of integers.

  Returns:
    A list of integers with the even numbers sorted in ascending order and the odd numbers in their original positions.
  """

  # Create a list to store the even numbers.
  even_numbers = []
  for i in range(len(arr)):
    if arr[i] % 2 == 0:
      even_numbers.append(arr[i])

  # Sort the even numbers in ascending order.
  even_numbers.sort()

  # Create a new list to store the sorted array.
  sorted_array = []
  for i in range(len(arr)):
    if arr[i] % 2 == 0:
      sorted_array.append(even_numbers.pop(0))
    else:
      sorted_array.append(arr[i])

  return sorted_array
