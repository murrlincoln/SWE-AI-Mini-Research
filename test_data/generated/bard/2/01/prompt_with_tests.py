class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  def push(self, new_data):
    new_node = Node(new_data)
    new_node.next = self.head
    self.head = new_node

  def reverse_linked_list(self):
    prev = None
    current = self.head
    while current is not None:
      next = current.next
      current.next = prev
      prev = current
      current = next
    self.head = prev

  def print_list(self):
    temp = self.head
    while temp is not None:
      print(temp.data, end=" ")
      temp = temp.next

if __name__ == '__main__':
  llist = LinkedList()
  llist.push(20)
  llist.push(4)
  llist.push(15)
  llist.push(85)

  print("Given linked list")
  llist.print_list()

  llist.reverse_linked_list()

  print("\nReversed Linked list")
  llist.print_list()
