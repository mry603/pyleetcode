#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        maxcon =0
        while left!=right:
            if height[left] > height[right]:
                con = height[right]*(right-left)
                right = right-1
            else:
                con = height[left]*(right-left)
                left = left+1
            if con>maxcon: maxcon =con
        return maxcon

# @lc code=end

