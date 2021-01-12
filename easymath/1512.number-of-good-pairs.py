#
# @lc app=leetcode id=1512 lang=python3
#
# [1512] Number of Good Pairs
#

# @lc code=start
class Solution:
    def numIdenticalPairs(self, nums):
        ''' (list of int) -> int
        calculate the number of good pairs: nums[i] == num[j] and i < j
        
        fake code:
        i in range(0,len()-1)
        j in range(i+1,len())
        if ==
        ans+1
        
        update:
        use dict, return n(n-1)/2
        '''
        number_of_time = {}
        ans = 0
        for i in range(len(nums)):
            if nums[i] not in number_of_time:
                number_of_time[nums[i]] = 1
            else:
                number_of_time[nums[i]] += 1
        
        for time in number_of_time:
            ans += number_of_time[time]*(number_of_time[time] - 1)//2
        
        return ans
        
        """
        ans = 0
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j]:
                    ans += 1

        return ans
        """


# @lc code=end

