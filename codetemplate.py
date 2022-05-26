# template


class Solution:
    def template(self,head):
        slow = fast = head
        while fast!=None and fast.next!=None:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                # add function
                return True
        return None