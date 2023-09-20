- Input: text = 'NEEDLE'
  Expected Output: 2
  
def count_vowels(text):
    
    # Initialize a counter variable
    num_vowels = 0
    
    # Base case: if the length of the string is 0, then return 0
    if len(text) == 0:
        return num_vowels
    
    # If the first letter of the string is a vowel, add 1 to the counter 
    if text[0] in ['a', 'e', 'i', 'o', 'u']:
        num_vowels += 1
        
    # Return the number of vowels by adding the number of vowels in the first letter with the number of vowels in the rest of the string
    return num_vowels + count_vowels(text[1:])