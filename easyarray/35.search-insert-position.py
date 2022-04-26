#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # for i in range(len(nums)):
        #     if nums[i]<target:
        #         pass
        #     else:
        #         return i
        # return i+1
        # nums.append(target)
        # nums.sort()
        # return nums.index(target)
        start = 0
        end = len(nums)
        while start<end:
            mid = ( start + end )//2
            if nums[mid] < target:
                start = mid +1
            elif nums[mid] == target:
                return mid
            else:
                end = mid
        return start

        
# @lc code=end

