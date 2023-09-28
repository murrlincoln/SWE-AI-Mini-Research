def sort_even_numbers(arr: List[int]) -> List[int]:
  even = []
  odd = []
  for num in arr:
    if num % 2 == 0:
      even.append(num)
    else:
      odd.append(num)
  
  even.sort()

  result = []
  i = 0
  j = 0
  for num in arr:
    if num % 2 == 0:
      result.append(even[i])
      i += 1
    else:
      result.append(odd[j])
      j += 1

  return result
