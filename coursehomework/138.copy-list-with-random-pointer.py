#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #Solution 1 O(n) O(n)
        # if not head: return None
        # dic ={}
        # node =head 
        # while node:
        #     newnode =Node(node.val)
        #     dic[node] = newnode
        #     node =node.next 
        # node = head 
        # while node:
        #     if node.next:
        #         dic[node].next = dic[node.next]
        #     if node.random:
        #         dic[node].random = dic[node.random]
        #     node =node.next
        # return dic[head]

        #soultion2 O(n) O(1)
        if not head: return None
        node = head
        while node:
            newnode =Node(node.val,node.next,node.random)
            node.next = newnode
            node =newnode.next
        node = head
        while node:
            if node.random:
                node.next.random =node.random.next
            node =node.next.next
        node = head
        newhead =Node(-1,None,None)
        newnode =newhead
        while node:
            newnode.next = node.next 
            newnode =newnode.next
            node.next = newnode.next
            node =node.next
        return newhead.next

        
# @lc code=end

