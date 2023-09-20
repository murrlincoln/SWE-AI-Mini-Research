def longest_substring_no_repeat(string):

    longest_so_far = ''
    current_substring = ''

    for index, letter in enumerate(string):
        if letter not in current_substring:
            current_substring += letter
            if len(current_substring) > len(longest_so_far):
                longest_so_far = current_substring
        else:
            current_substring = current_substring[current_substring.index(letter) + 1:] + letter
    
    return longest_so_far