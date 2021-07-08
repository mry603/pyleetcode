#
# @lc app=leetcode id=326 lang=python3
#
# [326] Power of Three
#

# @lc code=start
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        if n <= 0:
            return False
        epsilon = 0.0000000001
        logged = (log2(n)/log2(3) )%1
        return logged < epsilon #or logged > 1 - epsilon
        '''
        while n%3 == 0 and n>0:
            if n > 243:
                n = n / 243
            else:
                n = n / 3
        return n == 1
        '''
# @lc code=end

