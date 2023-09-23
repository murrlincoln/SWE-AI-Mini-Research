def function(a: str) -> int:
    vowels = "aeiou"
    count = 0
    for char in a:
        if char in vowels:
            count += 1
    return count if count > 1 else 0
