def reverse_linked_list(ll: List[int]) -> List[int]:
  """Reverses a linked list.

  Args:
    ll: A list of integers representing the linked list.

  Returns:
    A list of integers representing the reversed linked list.
  """

  previous = None
  current = ll.head
  while current:
    next_node = current.next
    current.next = previous
    previous = current
    current = next_node

  ll.head = previous
  return ll
