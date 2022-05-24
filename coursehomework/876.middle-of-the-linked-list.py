#
# @lc app=leetcode id=876 lang=python3
#
# [876] Middle of the Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #------two pointer------
        # if not head or not head.next: return head
        # fast = head.next
        # slow = head
        # while fast:
        #     for i in range(2):
        #         if fast:
        #             fast = fast.next
        #     slow = slow.next
        # return slow
        #
        #------reduce code------

        # slow =head
        # fast =head
        # while fast and fast.next:
        #     fast = fast.next.next
        #     slow = slow.next
        # return slow

        #------brute force with dic------
        dic = {}
        hlen =0
        while head:
            dic[hlen] =head
            hlen  = hlen +1
            head =head.next
        return dic[hlen//2]

        #follow up: 找到距离末端第几个位置的节点
        # -->快指针先移动然后慢指针移动
            
     
# @lc code=end

