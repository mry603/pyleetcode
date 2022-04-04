#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
    #     # value =[]
    #     # while head:
    #     #     value.append(head.val)
    #     #     head =head.next
    #     # first =0
    #     # while first < len(value)-1-first:
    #     #     if value[first] != value[len(value)-1-first]:
    #     #         return False
    #     #     else:
    #     #         first = first +1
    #     # return True

        fast = slow = head
        while fast and fast.next:
            fast =fast.next.next
            slow = slow.next
        
        fast = slow
        prev =None
        while fast:
            nextnode = fast.next
            fast.next = prev
            prev = fast
            fast = nextnode
        slow = head
        while prev:
            if slow.val !=prev.val:
                return False
            else:
                slow =slow.next
                prev =prev.next
        return True

            
        
# @lc code=end

