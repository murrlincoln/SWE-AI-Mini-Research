def longest_word(sentence: str) -> str:
    words = sentence.split()
    if not words:
        return ''
    longest = max(words, key=len)
    return longest
