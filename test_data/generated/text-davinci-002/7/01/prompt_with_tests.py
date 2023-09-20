- Input: m = 10, n = 15
  Expected Output: 10

def bitwise_AND(m, n): 
  
    AND = m 
      
    for i in range(m + 1, n + 1): 
        AND &= i 
          
    return AND