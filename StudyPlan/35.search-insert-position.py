#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        s = 0
        end = len(nums)-1
        while s<=end:
            mid = int(s+(end-s)/2)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                s = mid+1
            else:
                end = mid-1
        return end+1


# @lc code=end

