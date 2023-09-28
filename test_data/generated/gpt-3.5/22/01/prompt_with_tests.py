def find_longest_substring_without_repeating_characters(text: str) -> str:
    # Initialize variables to keep track of the current substring and its start index
    current_substring = ""
    start_index = 0
    
    # Create a dictionary to store the most recent index of each character
    char_index_map = {}
    
    # Initialize the length of the longest substring found so far
    max_length = 0
    
    # Initialize the starting index of the longest substring found so far
    max_start_index = 0
    
    # Iterate through the characters in the input string
    for i, char in enumerate(text):
        # If the character is already in the current substring
        if char in char_index_map and char_index_map[char] >= start_index:
            # Update the start index to the next index after the repeated character
            start_index = char_index_map[char] + 1
        
        # Update the index of the current character in the map
        char_index_map[char] = i
        
        # Add the current character to the current substring
        current_substring += char
        
        # Update the maximum length and starting index if a longer substring is found
        if len(current_substring) > max_length:
            max_length = len(current_substring)
            max_start_index = start_index
    
    # Extract and return the longest substring without repeating characters
    return text[max_start_index:max_start_index + max_length]
