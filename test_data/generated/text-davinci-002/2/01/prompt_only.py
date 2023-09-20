def reverseList(head): 
  
    if head is None: 
        return
   
    reverseList(head.next) 
    print(head.data) 
   
head = Node(1) 
head.next = Node(2) 
head.next.next = Node(3) 
head.next.next.next = Node(4) 
reverseList(head)