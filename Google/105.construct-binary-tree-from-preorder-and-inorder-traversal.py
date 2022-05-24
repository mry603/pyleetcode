#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder: return None
        node = TreeNode(preorder[0])
        rootindex = inorder.index(preorder[0])
        inorder_left = inorder[0:rootindex]
        inorder_right = inorder[rootindex+1:]
        preorder_left = preorder[1:len(inorder_left)+1]
        preorder_right = preorder[len(inorder_left)+1:]

        node.left = self.buildTree(preorder_left,inorder_left)
        node.right = self.buildTree(preorder_right,inorder_right)
        return node

        

        
# @lc code=end

