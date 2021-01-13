#
# @lc app=leetcode id=453 lang=python3
#
# [453] Minimum Moves to Equal Array Elements
#

# @lc code=start
class Solution:
    def minMoves(self, nums) :
        nummax = max(nums)#4
        numlen = len(nums)#4
        numsum = sum(nums)#10
        ans = nummax * numlen - numsum 
        while ans % (numlen-1) != 0:
            nummax += 1 
            ans = nummax * numlen - numsum
        return ans//(numlen-1)
# @lc code=end

