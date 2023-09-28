def longest_word(sentence: str) -> str:
    words = sentence.split()
    if not words:
        return ''
    
    longest = words[0]
    for word in words:
        if len(word) > len(longest):
            longest = word
    
    return longest
