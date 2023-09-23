def function(a: str) -> str:
    n = len(a)
    if n == 0:
        return ""
    
    start = 0
    max_len = 1
    cur_len = 1
    visited = [-1] * 256
    visited[ord(a[0])] = 0
    
    for i in range(1, n):
        prev_index = visited[ord(a[i])]
        
        if prev_index == -1 or (i - cur_len > prev_index):
            cur_len += 1
        else:
            if cur_len > max_len:
                max_len = cur_len
                start = i - cur_len
                
            cur_len = i - prev_index
        
        visited[ord(a[i])] = i
        
    if cur_len > max_len:
        max_len = cur_len
        start = n - cur_len
        
    return a[start:start + max_len]
