def function(a: str) -> str:
    if len(a) <= 1:
        return a
    
    vowels = "aeiouAEIOU"
    a_list = list(a)
    
    left, right = 0, len(a) - 1
    
    while left < right:
        while left < right and a_list[left] not in vowels:
            left += 1
        while left < right and a_list[right] not in vowels:
            right -= 1
        
        if left < right:
            a_list[left], a_list[right] = a_list[right], a_list[left]
            left += 1
            right -= 1
    
    return ''.join(a_list)
