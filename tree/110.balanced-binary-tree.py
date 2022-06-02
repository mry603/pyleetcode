#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        l = self.length(root.left)
        r = self.length(root.right)
        return abs(l-r)<2 and self.isBalanced(root.left) and self.isBalanced(root.right)

    def length(self,node):
        if node ==None :
            return 0
        return max(self.length(node.left),self.length(node.right))+1
                    
# @lc code=end

