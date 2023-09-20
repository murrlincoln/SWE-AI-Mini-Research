assert function([6, 0, 1, 2, 3, 4]) == [6, 4, 3, 2, 1, 0]
def function(x):
  if len(x) > 1:
    for i in range(1, len(x)): #iterate through list starting at index 1 until the length of that list 
      for j in range(i, 0, -1): #iterate through list from i (index 1) to 0, going in steps of -1
        if x[j] < x[j-1]: #if current value of list x is less than the value before it, we swap those values
          temp = x[j]
          x[j] = x[j-1] #swap the 2 values
          x[j-1] = temp
  print(x)
  return x