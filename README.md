# pyleetcode
Record leetcode solutions and ideas by python

Code Template:
Two pointers in Linkedlist:

Class solution:
  def template(self,head):
    slow = fast = head
    while fast!=None and fast.next!=None:
      fast = fast.next.next
      slow = slow.next
      if slow == fast: # todo
    return None
