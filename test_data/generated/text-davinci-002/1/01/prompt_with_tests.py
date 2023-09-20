- Input: 'aeiou'
  Expected Output: 'iouae'

def reverseVowels(string): 
      
    vowels = ('a', 'e', 'i', 'o', 'u')  
    string = list(string) 
    length = len(string) 
    string_copy = "" 
      
    i = 0
    j = length - 1
      
    while i < j:  
        if string[i] in vowels and string[j] in vowels: 
            string[i], string[j] = string[j], string[i] 
            i += 1
            j -= 1
              
        elif string[i] in vowels: 
            j -= 1
        elif string[j] in vowels: 
            i += 1
        else: 
            i += 1
            j -= 1
              
    return "".join(string)