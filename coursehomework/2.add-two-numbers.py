#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        TC:O(max(len(l1),len(l2))) ->O(max(m,n))
        SC:O(1)
        '''
        if not l1: return l2
        node1 =l1 
        node2 =l2 
        carry =0
        while node1 or node2:
            if not node2:
                y =0
            else:
                y= node2.val
                node2 =node2.next
            x= node1.val
            carry,node1.val = self.addnumber(x,y,carry)
            if not node1.next and (node2 or carry):
                node1.next = ListNode(0,None)
            node1 =node1.next
        return l1
           
    def addnumber(self, x,y,carry=0):
        #print(x,y,carry)
        return int((x+y+carry)/10), (x+y+carry)%10


        
# @lc code=end

