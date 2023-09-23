def reverse_linked_list(ll: List[int]) -> List[int]:
    """
    Reverses a singly linked list.

    Args:
        ll: A list of integers representing the linked list.

    Returns:
        A list of integers representing the reversed linked list.
    """

    # Initialize three pointers: previous, current, and next.
    previous = None
    current = ll
    next = None

    # Iterate through the linked list.
    while current is not None:
        # Store the next node.
        next = current.next

        # Update the next pointer of the current node to point to the previous node.
        current.next = previous

        # Update the previous and current pointers.
        previous = current
        current = next

    # The head of the reversed linked list is now the previous node.
    head = previous

    # Convert the linked list to a Python list.
    reversed_ll = []
    while head is not None:
        reversed_ll.append(head.data)
        head = head.next

    return reversed_ll

