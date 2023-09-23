def function(a: str, b: int) -> str:
    for i in range(len(a) - b + 1):
        sub = a[i:i+b]
        if len(set(sub)) == b:
            return sub
    return ''
