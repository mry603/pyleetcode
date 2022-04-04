#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        if head.next ==None:
            return False
        #method1 two pointers

        # slow = head
        # fast = head.next
        # while fast.next !=None and fast.next.next !=None:
        #     slow = slow.next
        #     fast = fast.next.next
        #     if slow == fast:
        #         return True
        # return False

        dictionary = {}
        node = head
        while node:
            if node in dictionary:
                return True
            else:
                dictionary[node] =True
            node = node.next
        return False
            
        
# @lc code=end

