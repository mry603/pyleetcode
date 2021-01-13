#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#

# @lc code=start
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        '''
        if max(nums) == len(nums):
            for i in range(max(nums)):
                if i not in nums:
                    return i
        else:
            return len(nums)
        '''
        
        if not max(nums) == len(nums):
            return len(nums)
        else:
            nums.sort()
            for i in range(len(nums)):
                if i != nums[i]:
                    return i

# @lc code=end

