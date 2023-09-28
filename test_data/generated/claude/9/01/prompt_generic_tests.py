def function(a: Dict[int, List[int]], b: int) -> List[int]:
  result = [b]
  seen = set()
  
  def visit(n):
    if n not in seen:
      seen.add(n)
      result.append(n)
      for m in a.get(n, []):
        visit(m)

  visit(b)
  return result
