#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = max(nums)
        subarray_sum = 0 
        for i in range(len(nums)):
            subarray_sum = subarray_sum + nums[i]
            if subarray_sum < 0:
                subarray_sum = 0
            else:
                if subarray_sum > ans:
                    ans = subarray_sum
        return ans

         
        
# @lc code=end

