#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        Fail 20 + 50
        TC: DP:O(n^2),BS: O(nlogn)
        SC: DP:O(n),BS:O(n)
        '''
        #Solution 1: DP
        if not nums: return 0
        dp =[1]*len(nums)
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i]>nums[j] and dp[i] < dp[j]+1:
                    dp[i] = dp[j]+1
        return max(dp)

        
        #Solution 2 :binary search
        lis = [nums[0]]
        for i in range(1,len(nums)):
            if nums[i]>lis[-1]: 
                lis.append(nums[i]) 
            else:
                l =0
                r =len(lis)-1
                pos =0
                while l<=r:
                    mid = int(l+(r-l)/2)
                    if lis[mid]>=nums[i]:
                        pos =mid
                        r= mid-1
                    else:
                        l =mid+1
                    lis[pos] =nums[i]
        return len(lis)

        
# @lc code=end

