def longest_word(sentence: str) -> str:
    words = sentence.split()
    return max(words, key=len)
