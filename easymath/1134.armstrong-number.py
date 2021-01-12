#
# @lc app=leetcode id=1134 lang=python3
#
# [1134] Armstrong Number
#

# @lc code=start
class Solution:
    def isArmstrong(self, N) :
        '''(int) -> bool
        return true if k-th power of each digit sums to N
        '''
        ans = 0
        M = N
        k = len(str(N))
        while M // 10 != 0 or M % 10 != 0:
            ans += (M % 10) ** k
            M = M // 10
        #print(N,k,ans)
        return N == ans
        
# @lc code=end

