def count_vowels(text: str) -> int:
    # Initialize a variable to keep track of the vowel count
    vowel_count = 0
    
    # Iterate through each character in the input text
    for char in text:
        # Check if the character is a vowel (case-insensitive)
        if char.lower() in "aeiou":
            vowel_count += 1
    
    return vowel_count
