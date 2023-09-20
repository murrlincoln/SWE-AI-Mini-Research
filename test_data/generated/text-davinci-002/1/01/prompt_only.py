"

def reverseVowels(input): 
  
  vowels = ('a', 'e', 'i', 'o', 'u') 
  
  input = list(input) 
   
  left = 0
  right = len(input) - 1
   
  while left < right: 
  
    if input[left] not in vowels: 
      left += 1
    elif input[right] not in vowels: 
      right -= 1
    else: 
      input[left], input[right] = input[right], input[left] 
      left += 1
      right -= 1
   
  return ''.join(input)