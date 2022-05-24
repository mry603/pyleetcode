#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # l =head
        # mid = None
        # while mid:
        #     r =mid.next
        #     mid.next = l
        #     l = mid
        #     mid = r
        # return l
        return self.reverseNode(head,None)
    def reverseNode(self, head,prev=None):
        if head == None:
            return prev
        else:
            newhead = head.next
            head.next = prev
            return self.reverseNode(newhead,head)

        
# @lc code=end

