#
# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # stack = [(p,q)]
        # while len(stack):
        #     pnode,qnode = stack.pop()
        #     if pnode==None and qnode==None:
        #         pass
        #     elif pnode==None or qnode==None:
        #         return False
        #     else:
        #         if pnode.val != qnode.val:
        #             return False
        #         else:
        #             stack.append((pnode.left,qnode.left))
        #             stack.append((pnode.right,qnode.right))
        # return True
        if p==None and q==None: 
            return True
        elif p==None or q==None:
            return False
        else:
            return p.val ==q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
            
            


        
# @lc code=end

