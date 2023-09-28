def function(a: str) -> int:
    vowel_count = 0
    vowels = "aeiouAEIOU"
    
    for char in a:
        if char in vowels:
            vowel_count += 1
    
    return vowel_count
