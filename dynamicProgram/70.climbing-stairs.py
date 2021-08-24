#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        x = 1 
        y = 2
        if n == 1:
            return x
        if n == 2:
            return y
        if n == 3:
            return x+y
        
        for i in range (3,n):
            z = x + y
            x = y
            y = z
        return x+y
        
# @lc code=end

