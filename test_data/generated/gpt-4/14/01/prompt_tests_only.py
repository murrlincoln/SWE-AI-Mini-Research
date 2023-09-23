def longest_word(sentence: str) -> str:
    words = sentence.split()
    if not words:
        return ''
    return max(words, key=len)
