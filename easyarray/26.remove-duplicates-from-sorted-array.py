#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # i =1
        # while i<len(nums):
        #     if nums[i] ==nums[i-1]:
        #         nums.pop(i)
        #     else:
        #         i = i+1
        i = 0
        for j in range(1,len(nums)):
            if nums[j] == nums[i]:
                pass
            else:
                i =i+1
                nums[i] = nums[j]
        return i+1


        
# @lc code=end

