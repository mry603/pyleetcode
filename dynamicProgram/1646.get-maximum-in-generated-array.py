#
# @lc app=leetcode id=1646 lang=python3
#
# [1646] Get Maximum in Generated Array
#

# @lc code=start
class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        nums = [0,1]
        if n<2: return nums[n]
        for i in range(2,n+1):
            if i%2 == 0:
                nums.append(nums[int(i/2)])
            else:
                nums.append(nums[int(i/2)]+nums[int(i/2)+1])
        return max(nums)
        
# @lc code=end

