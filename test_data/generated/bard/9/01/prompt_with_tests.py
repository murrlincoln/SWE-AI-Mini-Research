def depth_first_search(graph: Dict[int, List[int]], start: int) -> List[int]:
  """Performs a depth-first search on a graph represented as an adjacency list.

  Args:
    graph: A dictionary mapping integers to lists of integers, where each list
      represents the adjacent nodes of the corresponding integer.
    start: The start node for the search.

  Returns:
    A list of integers in the order in which they were visited by the search.
  """

  visited = set()
  result = []

  def dfs(node: int):
    if node not in visited:
      visited.add(node)
      result.append(node)
      for neighbor in graph[node]:
        dfs(neighbor)

  dfs(start)
  return result
