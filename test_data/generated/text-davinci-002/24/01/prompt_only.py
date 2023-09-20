def longest_palindromic_substring(word):
    max_length = 1
 
    start = 0
    length = len(word)
 
    low = 0
    high = 0
 
    for i in xrange(1, length):
 
        low = i - 1
        high = i
        while low >= 0 and high < length and word[low] == word[high]:
            if high - low + 1 > max_length:
                start = low
                max_length = high - low + 1
            low -= 1
            high += 1
 
        low = i - 1
        high = i + 1
        while low >= 0 and high < length and word[low] == word[high]:
            if high - low + 1 > max_length:
                start = low
                max_length = high - low + 1
            low -= 1
            high += 1
 
    print "Longest palindrome substring is:", word[start:start + max_length]
 
    return max_length