def function(a: Dict[int, List[int]], b: int) -> List[int]:
  """Returns a list of all integers reachable from b in the graph represented by a.

  Args:
    a: A dictionary mapping integers to lists of integers, where each list represents
      the neighbors of the corresponding integer in the graph.
    b: The starting integer.

  Returns:
    A list of all integers reachable from b in the graph.
  """

  visited = set()
  queue = [b]

  while queue:
    current_node = queue.pop(0)
    visited.add(current_node)

    for neighbor in a[current_node]:
      if neighbor not in visited:
        queue.append(neighbor)

  return list(visited)
