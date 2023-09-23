def function(a: int) -> int:
  if a == 0:
    return 1
  else:
    return a * function(a - 1)
