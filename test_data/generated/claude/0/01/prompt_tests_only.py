def sort_even_numbers(arr: List[int]) -> List[int]:
  even = []
  odd = []
  for num in arr:
    if num % 2 == 0:
      even.append(num)
    else:
      odd.append(num)
  
  even.sort()
  odd.sort()

  result = []
  for i in range(len(arr)):
    if i % 2 == 0:
      result.append(even[i//2]) 
    else:
      result.append(odd[i//2])

  return result
