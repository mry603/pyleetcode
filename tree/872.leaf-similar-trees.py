#
# @lc app=leetcode id=872 lang=python3
#
# [872] Leaf-Similar Trees
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(root)->list:
            stack=[]
            mylist =[]
            while stack or root:
                while root:
                    stack.append(root)
                    root = root.left
                
                root = stack.pop()
                if not root.left and not root.right:
                    mylist.append(root.val)
                root = root.right
            return mylist
        return dfs(root1) == dfs(root2)

        
# @lc code=end

