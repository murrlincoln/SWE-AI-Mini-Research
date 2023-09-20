def reverse_linked_list(linked_list):
  current = linked_list.head
  previous = None
  next = current.next

  while current:
    current.next = previous
    previous = current
    current = next
    if current:
      next = current.next

  linked_list.head = previous