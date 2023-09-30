def function(a, b):
    curr = ''
    for c in a:
        curr += c
        if len(curr) == b:
            return curr
    return ''
