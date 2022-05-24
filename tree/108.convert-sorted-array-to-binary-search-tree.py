#
# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums: return None
        depth = len(nums)//2
        head = TreeNode(nums[depth])
        head.left = self.sortedArrayToBST(nums[:depth])
        head.right = self.sortedArrayToBST(nums[depth+1:])
        return head

        
# @lc code=end

