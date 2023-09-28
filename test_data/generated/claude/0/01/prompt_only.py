def sort_even_numbers(arr):
  even_indices = []
  for i, num in enumerate(arr):
    if num % 2 == 0:
      even_indices.append(i)

  even_nums = [arr[i] for i in even_indices]
  even_nums.sort()

  for i, idx in enumerate(even_indices):
    arr[idx] = even_nums[i]

  return arr
