def depth_first_search(graph, start):
    visited = set()
    stack = [start]
    
    result = []
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            result.append(vertex)
            stack.extend(graph[vertex])
            
    return result
