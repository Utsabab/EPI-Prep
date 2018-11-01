def find_if(head):
  if head.next = None:
    return False 
  else:
    slow_head = self.head
    fast_head = self.head
    while (slow_head and fast_head and fast_head.next):
      slow_head = slow_head.next
      fast_head = fast_head.next.next
      if slow_head == fast_head:
        return True
    return False

