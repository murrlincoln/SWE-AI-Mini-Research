def reverse_vowels(s: str) -> str:
    # Helper function to check if a character is a vowel
    def is_vowel(char):
        return char in 'aeiouAEIOU'
    
    # Convert the string to a list of characters to make modifications easier
    s_list = list(s)
    
    # Initialize pointers for the left and right ends of the string
    left, right = 0, len(s_list) - 1
    
    # Continue until the pointers meet
    while left < right:
        # Find the next vowel from the left
        while left < right and not is_vowel(s_list[left]):
            left += 1
        
        # Find the next vowel from the right
        while left < right and not is_vowel(s_list[right]):
            right -= 1
        
        # Swap the vowels
        s_list[left], s_list[right] = s_list[right], s_list[left]
        
        # Move the pointers inward
        left += 1
        right -= 1
    
    # Convert the list back to a string and return
    return ''.join(s_list)
