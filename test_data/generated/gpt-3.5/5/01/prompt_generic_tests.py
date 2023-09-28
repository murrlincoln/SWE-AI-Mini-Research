def function(a: str, b: str) -> int:
    count = 0
    i = 0

    while i < len(a):
        if a[i:i + len(b)] == b:
            count += 1
            i += len(b)
        else:
            i += 1

    return count
