#
# @lc app=leetcode id=977 lang=python3
#
# [977] Squares of a Sorted Array
#

# @lc code=start


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # 从中间开始--多一个遍历
        # ans = []
        # if nums[0]>=0: 
        #     for item in nums:
        #         ans.append(item**2)
        #     return ans
        # if nums[len(nums)-1] <0: 
        #     for i in range(len(nums)-1,-1,-1):
        #         ans.append(nums[i]**2)
        #     return ans
        # for i in range(1,len(nums)):
        #     if nums[i-1]<0 and nums[i]>=0:
        #         break
        # #[-3,-1,0]
        # l = i-1 # <0 1
        # r = i   # >=0   2 3
        # while l>=0 and r<len(nums):
        #     if 0-nums[l] < nums[r]:
        #         ans.append(nums[l]**2)
        #         l = l-1
        #     else:
        #         ans.append(nums[r]**2)
        #         r = r+1
        # if l >=0:
        #     for i in range(l,-1,-1):
        #         ans.append(nums[i]**2)
        # elif r <len(nums):
        #     for i in range(r,len(nums)):
        #         ans.append(nums[i]**2)
        # return ans

        ##从两头开始,没有复杂的过程
        ans =[0]*len(nums)
        l = 0
        r =len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            if abs(nums[l]) < abs(nums[r]):
                ans[i] = nums[r]**2
                r = r-1
            else:
                ans[i] = nums[l]**2
                l = l+1
        return ans


# @lc code=end

