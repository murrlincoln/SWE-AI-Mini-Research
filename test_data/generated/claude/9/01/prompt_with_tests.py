def depth_first_search(graph, start):
  visited = set()
  stack = [start]

  result = []
  
  while stack:
    current = stack.pop()
    if current not in visited:
      visited.add(current)
      result.append(current)
      
      for neighbor in graph[current]:
        stack.append(neighbor)
        
  return result
