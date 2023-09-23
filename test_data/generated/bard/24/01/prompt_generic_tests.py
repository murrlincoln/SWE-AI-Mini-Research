def function(a: str) -> str:
    n = len(a)
    start = 0
    end = 0
    max_len = 1
    for i in range(n):
        for j in range(i, n):
            while i >= 0 and j < n and a[i] == a[j]:
                i -= 1
                j += 1
            if j - i - 1 > max_len:
                start = i + 1
                end = j - 1
                max_len = j - i - 1
    return a[start:end + 1]
