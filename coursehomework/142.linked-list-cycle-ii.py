#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # ------hashtable-------
        dic ={}
        index =0
        while head:
            if head in dic:
                return head
            dic[head] = index
            head = head.next 
            index = index +1
        return None

        # TC:O(n) SC: O(n) 

        #------two pointers------
        slow = fast = head
        while fast!=None and fast.next!=None:
            fast = fast.next.next
            slow = slow.next
            if slow == fast: break
        if slow != fast or head == None or head.next ==None: 
            return None
        else:
            while head !=slow:
                head = head.next
                slow = slow.next
        return slow

        #TC:O(n) SC: O(1)
            

        
# @lc code=end

