def depth_first_search(graph: Dict[int, List[int]], start: int) -> List[int]:
  """Performs a depth-first search of the given graph starting at the given node.

  Args:
    graph: A dictionary mapping nodes to their adjacent nodes.
    start: The node to start the search from.

  Returns:
    A list of the nodes visited in the order they were visited.
  """

  visited = set()
  result = []

  def dfs(node):
    if node in visited:
      return
    visited.add(node)
    result.append(node)
    for neighbor in graph[node]:
      dfs(neighbor)

  dfs(start)
  return result
