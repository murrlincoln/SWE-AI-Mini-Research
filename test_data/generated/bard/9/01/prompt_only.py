def depth_first_search(graph: Dict[int, List[int]], start: int) -> List[int]:
  """
  Performs a depth-first search on a graph represented as an adjacency list.

  Args:
    graph: A dictionary mapping vertices to their adjacent vertices.
    start: The vertex to start the search from.

  Returns:
    A list of the vertices visited in the order they were visited.
  """

  visited = set()
  stack = [start]

  while stack:
    node = stack.pop()

    if node not in visited:
      visited.add(node)

      for neighbor in graph[node]:
        if neighbor not in visited:
          stack.append(neighbor)

  return list(visited)
