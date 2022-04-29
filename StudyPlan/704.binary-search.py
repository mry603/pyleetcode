#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # first = 0
        # end = len(nums)
        # while first < end:
        #     mid = (first +end)//2
        #     if nums[mid] == target:
        #         return mid
        #     elif nums[mid]> target:
        #         end = mid
        #     else:
        #         first = mid+1
        # return -1
        first = 0
        end = len(nums) - 1
        while(first <= end):
            mid = int((first + end)//2)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                first = mid + 1
            else:
                end = mid - 1
        return -1

        
# @lc code=end

