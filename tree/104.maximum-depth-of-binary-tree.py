#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        maxdep =1
        dep = 1
        stack = [(root,dep)]
        while stack:
            root,dep = stack.pop()
            if root:
                if root.left:
                    stack.append((root.left,dep+1))
                if root.right:
                    stack.append((root.right,dep+1))
            if dep>maxdep: maxdep =dep
        return maxdep
# @lc code=end

