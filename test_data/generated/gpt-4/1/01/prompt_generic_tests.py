def function(a: str) -> str:
    vowel = 'aeiouAEIOU'
    first_vowel_index = None
    last_vowel_index = None
    
    for i, char in enumerate(a):
        if char in vowel:
            first_vowel_index = i
            break
    
    for i, char in reversed(list(enumerate(a))):
        if char in vowel:
            last_vowel_index = i
            break
    
    if first_vowel_index is not None and last_vowel_index is not None:
        a_list = list(a)
        a_list[first_vowel_index], a_list[last_vowel_index] = a_list[last_vowel_index], a_list[first_vowel_index]
        return ''.join(a_list)
    else:
        return a
