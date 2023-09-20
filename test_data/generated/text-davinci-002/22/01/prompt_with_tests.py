- Input: 'pwwkew'
  Expected Output: 'wke'

def longest_substring_without_repeating_characters(input):
    longest_substring = ""
    current_substring = ""

    for i, c in enumerate(input):
        if c not in current_substring:
            current_substring += c
        else:
            if len(current_substring) > len(longest_substring):
                longest_substring = current_substring
            current_substring = c

    return longest_substring