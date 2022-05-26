#
# @lc app=leetcode id=160 lang=python3
#
# [160] Intersection of Two Linked Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # ---hash table---
        # node =headA
        # dic = {}
        # while node:
        #     dic[node] =True
        #     node =node.next
        # node = headB
        # while node:
        #     if node in dic:
        #         return node
        #     else:
        #         node = node.next
        # return None

        #TC: O(m+n) SC:O(n)

        # two-pointers
        node1 = headA
        node2 = headB
        flag1 = False
        flag2 = False
        while (node1 or flag1 ==False) and (node2 or flag2 ==False) :
            if node1 == node2:
                return node1
            else:
                if node1:
                    node1 = node1.next
                elif flag1 == False:
                    flag1 =True
                    node1 =headB
                if node2:
                    node2 = node2.next
                elif flag2 == False:
                    flag2 =True
                    node2 =headA
        return None

        #TC: O(m+n) SC:O(1)

        
# @lc code=end

