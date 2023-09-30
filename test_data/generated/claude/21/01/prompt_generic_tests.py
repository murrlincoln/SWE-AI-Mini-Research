def function(a: str) -> str:
    return max(set(a), key=a.count)
