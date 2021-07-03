#
# @lc app=leetcode id=342 lang=python3
#
# [342] Power of Four
#

# @lc code=start
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        '''
        return num > 0 and log2(num) % 2 == 0

        return num > 0 and num & (num - 1) == 0 and num & 0xaaaaaaaa == 0
        
        '''
        if n & (n - 1) == 0 and n != 0:
            nbin = bin(n)[2:]
            return len(nbin)%2 == 1
        else:
            return False
# @lc code=end

