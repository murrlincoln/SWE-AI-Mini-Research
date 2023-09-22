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

  # Iterate over the original array and insert the even numbers from the sorted list at the appropriate positions.
  odd_index = 0
  even_index = 0
  while odd_index < len(arr) and even_index < len(even_numbers):
    if arr[odd_index] % 2 == 1:
      sorted_array.append(arr[odd_index])
      odd_index += 1
    else:
      sorted_array.append(even_numbers[even_index])
      even_index += 1

  # Add any remaining even numbers to the sorted list.
  while even_index < len(even_numbers):
    sorted_array.append(even_numbers[even_index])
    even_index += 1

  return sorted_array
