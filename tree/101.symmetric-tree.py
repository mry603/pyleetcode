#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
    #     p =root.left 
    #     q = root.right
    #     return self.helper(p,q) 

    # def helper(self,pnode,qnode):
    #     if not pnode and not qnode:
    #         return True
    #     elif not qnode or not pnode:
    #         return False
    #     else:
    #         return pnode.val == qnode.val and self.helper(pnode.left,qnode.right) and self.helper(pnode.right,qnode.left)
        stack =[(root.left,root.right)]
        while stack:
            p,q = stack.pop()
            if not p and not q:
                pass
            elif not p or not q:
                return False
            else:
                if p.val!=q.val: return False
                stack.append((p.left,q.right))
                stack.append((p.right,q.left))
        return True   

        
# @lc code=end

