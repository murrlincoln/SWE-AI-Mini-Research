def firstNonRepeatingChar(string): 
      
    # Initialize all characters as repeating 
    # Once a character is found to be non 
    # repeating, it is marked as visited 
    repeated = [False for _ in range(256)] 
      
    # Mark first character as visited 
    repeated[ord(string[0])] = True
      
    # Find the first non repeating 
    for i in range(1, len(string)): 
        if not repeated[ord(string[i])]: 
            return string[i] 
        repeated[ord(string[i])] = True
      
    return '$'