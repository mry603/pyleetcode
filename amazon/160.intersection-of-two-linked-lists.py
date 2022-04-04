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



# class Solution:
#     def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # dic = {}
        # nodea =headA
        # while nodea:
        #     dic[nodea] = nodea.val
        #     nodea = nodea.next
        # nodeb = headB
        # while nodeb:
        #     if nodeb in dic:
        #         return nodeb
        #     else:
        #         nodeb = nodeb.next
        # return None
        # nodea = headA
        # nodeb = headB
        # flaga =2
        # flagb =2
        # while (flagb or flaga):
        #     if nodea ==nodeb:
        #         return nodea
        #     if nodea.next:
        #         nodea = nodea.next
        #     else:
        #         nodea = headB
        #         flaga =flaga -1
        #     if nodeb.next:
        #         nodeb = nodeb.next
        #     else:
        #         nodeb = headA
        #         flagb =flagb-1
        # return None

class Solution:
    def zeroreverse(self,head: ListNode)-> None:
        while head:
            head.val = head.val*(-1)
            head = head.next


    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        self.zeroreverse(headA)
        nodeb = headB
        while nodeb:
            if nodeb.val<0: break
            nodeb = nodeb.next
        self.zeroreverse(headA)
        return nodeb
        
# @lc code=end

