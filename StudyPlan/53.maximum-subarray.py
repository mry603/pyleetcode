#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # if len(nums) <=1:
        #     return sum(nums)
        # maxsum = max(max(nums),sum(nums))
        # l = 0
        # r = len(nums)-1
        # while l<=r:
        #     if maxsum < sum(nums[l:r]):
        #         maxsum = sum(nums[l:r])
        #     if nums[l]<nums[r]:
        #         l += 1
        #     else:
        #         r -= 1
        # return maxsum
        cur_max = glo_max = nums[0]
        for nums in nums[1:]:
            cur_max = max(nums, cur_max + nums)
            glo_max = max(cur_max, glo_max)
        return glo_max
        
# @lc code=end

