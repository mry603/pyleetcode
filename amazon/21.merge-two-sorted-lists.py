#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        #method1
        # node1 =list1
        # node2 =list2
        # if node2.val <node1.val:
        #     node = node2
        #     node2 = node.next
        # else:
        #     node = node1
        #     node1 = node.next
        # head = node
        # while node.next is not None:
        #     if node1.val > node2.val:
        #         node.next = node2
        #         node2 = node2.next
        #     else:
        #         node.next = node1
        #         node1 = node1.next
        #     node = node.next
        # if node1:
        #     node.next = node1
        # if node2:
        #     node.next = node2
        # return head

        #method2
        if list1.val <list2.val:
            list1.next = self.mergeTwoLists(list1.next,list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1,list2.next)
            return list2



# @lc code=end

