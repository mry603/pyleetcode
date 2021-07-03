#
# @lc app=leetcode id=231 lang=python3
#
# [231] Power of Two
#

# @lc code=start
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        '''
        if n<0:
            return False
        nbin = bin(n)[2:]
        if sum([int(item) for item in nbin]) == 1:
            return True
        else:
            return False



        if n == 0:
            return False
        else:
            return n & (-n) == n
         

        if n == 0:
            return False
        else:
            return n & (n-1) == 0
        '''
        return n>0 and log2(n) == int(log2(n))
# @lc code=end

