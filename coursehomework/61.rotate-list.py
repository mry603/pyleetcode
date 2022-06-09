#
# @lc app=leetcode id=61 lang=python3
#
# [61] Rotate List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        '''
        TC:O(n)
        SC:O(1)
        '''
        if not head or not head.next or not k: return head
        fast =head 
        length =1
        while fast.next:
            length = length +1
            fast =fast.next
        step = length-k%length
        if step == length: return head
        fast.next =head
        for i in range(step):
            fast = fast.next
        head =fast.next
        fast.next = None
        return head
        
# @lc code=end

