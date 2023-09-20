- Input: [5, 1, 4, 2, 3]
  Expected Output: [1, 2, 3, 4, 5]
- Input: [5, 2, 1, 4, 3]
  Expected Output: [1, 2, 3, 4, 5]

def bubble_sort(array): 
  
    # Traverse through all array elements 
    for i in range(len(array)): 
  
        # Last i elements are already in place 
        for j in range(0, len(array)-i-1): 
  
            # traverse the array from 0 to n-i-1 
            # Swap if the element found is greater 
            # than the next element 
            if array[j] > array[j+1]: 
                array[j], array[j+1] = array[j+1], array[j]