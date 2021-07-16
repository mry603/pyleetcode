#
# @lc app=leetcode id=172 lang=python3
#
# [172] Factorial Trailing Zeroes
#

# @lc code=start
class Solution:
    def trailingZeroes(self, n: int) -> int:
        num2 = 0
        muti2= 2
        num5 = 0
        muti5= 5
        '''
        while (muti2<=n):
            num2 = num2 + n//muti2
            muti2 = muti2 * 2
        '''
        while(muti5<=n):
            num5 = num5 + n//muti5
            muti5 = muti5 * 5
        return num5

        
# @lc code=end

