def sort_even_numbers(nums):
  even = []
  odd = []
  for i in nums:
    if i % 2 == 0:
      even.append(i)
    else:
      odd.append(i)
  sorted_even = sorted(even)
  sorted_odd = sorted(odd)
  for j in sorted_odd:
    sorted_even.append(j)
  return sorted_even