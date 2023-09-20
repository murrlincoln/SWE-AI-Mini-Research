def first_non_repeating(given_string): 
  
    seen_letter = {}
  
    for idx, letter in enumerate(given_string): 
        if letter not in seen_letter: 
            seen_letter[letter] = (1, idx)
        else: 
            seen_letter[letter] = (seen_letter[letter][0] + 1, seen_letter[letter][1])
              
    final_letters = []
    for key, value in seen_letter.items(): 
        if value[0] == 1: 
            final_letters.append((key, value[1]))
              
    not_repeated = sorted(final_letters, key = lambda x: x[1])
    if not_repeated: 
        return not_repeated[0][0]
    else: 
        return None