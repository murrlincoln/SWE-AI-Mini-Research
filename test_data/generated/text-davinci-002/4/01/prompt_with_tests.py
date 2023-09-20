- Input: [0, 1, 2, 3, 4]
  Expected Output: 12

def maxProduct(lst): 
 
    if (len(lst) < 2): 
        print("No maximum product") 
        return
 
    a = max(lst[0], lst[1]) 
    b = min(lst[0], lst[1]) 
 
    for i in range(2, len(lst)): 
        if (lst[i] >= a): 
            b = a 
            a = lst[i] 
        elif (lst[i] >= b): 
            b = lst[i] 
    return a * b