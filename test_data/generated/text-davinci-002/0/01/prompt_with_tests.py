def sortEvenOdd(arr): 
  
    # Initialize two empty arrays 
    left = [] 
    right = [] 
  
    # Split the array in two parts 
    for i in range(0, len(arr)): 
        if arr[i]%2 == 0: 
            left.append(arr[i]) 
        else: 
            right.append(arr[i]) 
      
    # Sort the 'left' array in ascending order 
    # using MergeSort 
    left = mergeSort(left) 
  
    # Merge both the arrays and store 
    # it in 'arr' 
    arr = [] 
    j, k = 0, 0
  
    # Merge both left[] and right[] 
    # into arr[] 
    while j < len(left) and k < len(right): 
        if left[j] <= right[k]: 
            arr.append(left[j]) 
            j+= 1
        else: 
            arr.append(right[k]) 
            k+= 1
  
    # Store remaining elements 
    # of left[] 
    while j < len(left): 
        arr.append(left[j]) 
        j+= 1
    # Store remaining elements 
    # of right[] 
    while k < len(right): 
        arr.append(right[k]) 
        k+= 1
  
    return arr