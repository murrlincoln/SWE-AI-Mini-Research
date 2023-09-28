def function(a: List[int]) -> List[int]:
  for i in range(len(a)):
    for j in range(i+1, len(a)):
      if a[i] > a[j]:
        a[i], a[j] = a[j], a[i]
  return a
