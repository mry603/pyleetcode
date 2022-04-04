# @before-stub-for-debug-begin

# @before-stub-for-debug-end

#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #method1
        # ans = [0,0]
        # for i in range(len(nums)-1):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j] == target:
        #             ans[0] = i
        #             ans[1] = j
        #             return ans

        #method2
        # ans = [0,0]
        # for i in range(len(nums)-1):
        #     if target - nums[i] in nums:
        #         f = 0
        #         for k in range(nums.count(target - nums[i])):
        #             j = nums.index(target - nums[i],f,len(nums))
        #             if j != i:
        #                 ans[0] = i
        #                 ans[1] = j
        #                 return ans
        #             else:
        #                 f = j+1
        
        #method3
         map = {}
         for i, n in enumerate(nums):
             diff = target - n
             if diff in map:
                 print( map[diff], i)
             map[n] = i
             print(map)
         return

                    

        
# @lc code=end


