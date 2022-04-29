#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # dic = {}
        # for item in nums:
        #     if item in dic:
        #         return True
        #     else:
        #         dic[item] = True
        # return False
        # nums.sort()
        # for i in range(1,len(nums)):
        #     if nums[i] == nums[i-1]:
        #         return True
        # return False
         return len(nums) != len(set(nums))
        

# @lc code=end

