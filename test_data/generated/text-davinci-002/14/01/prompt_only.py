def longest_word(sentence): 
    longest = ""
    for word in sentence.split():
        if len(word) > len(longest):
            longest = word
    return longest