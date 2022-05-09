#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head .next ==None:
            return None
        fast = head
        for i in range(n):
            fast = fast.next 
        if not fast:
            return head.next
        slow = head
        while fast .next !=None:
            slow = slow.next
            fast = fast.next
        if n==1:
            slow.next = None
        else:
            slow.next = slow.next.next

        return head


        
# @lc code=end

