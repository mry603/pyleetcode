#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # i = 0 
        # j = len(nums)-1
        # while i <= j:
        #     if nums[i]!= val:
        #         i = i+1
        #     else:
        #         nums[i] = nums[j]
        #         j = j-1
        # return i
        i= 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
            else:
                i = i+1

        
# @lc code=end

